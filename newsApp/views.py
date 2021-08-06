from django.shortcuts import render
from .models import MyNew
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from pyquery import PyQuery as pq
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from helpers import get_page_list, ajax_required
from comment.forms import CommentForm
from comment.models import Comment2
def news(request, newName):
    # 解析请求的新闻类型
    submenu = newName
    if newName == 'company':
        newName = '企业要闻'
    elif newName == 'industry':
        newName = '行业新闻'
    else:
        newName = '通知公告'
    # 从数据库获取、过滤和排序数据
    newList = MyNew.objects.all().filter(
        newType=newName).order_by('-publishDate')
    for mynew in newList:
        html = pq(mynew.description)  # 使用pq方法解析html内容
        mynew.mytxt = pq(html)('p').text()  # 截取html段落文字
    # 分页
    p = Paginator(newList, 5)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        newList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'newList.html', {
            'active_menu': 'news',
            'sub_menu': submenu,
            'newName': newName,
            'newList': newList,
            'pageData': pageData,
        })


def newDetail(request, id):
    mynew = get_object_or_404(MyNew, id=id)
    mynew.views += 1
    mynew.save()
    form = CommentForm()
    comments = Comment2.objects.filter(news_id=id).order_by('-timestamp').all()
    return render(request, 'newDetail.html', {
        'active_menu': 'news',
        'mynew': mynew,
        'form':form,
        'comments':comments
    })


def search(request):
    keyword = request.GET.get('keyword')
    newList = MyNew.objects.filter(title__icontains=keyword)
    newName = "The search result about " + "\"" + keyword + "\""
    return render(request, 'searchList.html', {
        'active_menu': 'news',
        'newName': newName,
        'newList': newList,
    })
@ajax_required
@require_http_methods(["POST"])
def like(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "Please log in firstly"})
    news_id = request.POST['news_id']
    news = MyNew.objects.get(pk=news_id)
    user = request.user
    news.switch_like(user)
    return JsonResponse({"code": 0, "likes": news.count_likers(), "user_liked": news.user_liked(user)})


@ajax_required
@require_http_methods(["POST"])
def collect(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "Please log in firstly"})
    news_id = request.POST['news_id']
    news = MyNew.objects.get(pk=news_id)
    user = request.user
    news.switch_collect(user)
    return JsonResponse({"code": 0, "collects": news.count_collecters(), "user_collected": news.user_collected(user)})
