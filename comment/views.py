from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import *
from django.template.loader import render_to_string
from ratelimit.decorators import ratelimit
from newsApp.forms import CommentForm as CommentForm2
from newsApp.models import MyNew
from comment.models import Comment2
@ratelimit(key='ip', rate='2/m')
def submit_comment_news(request,pk):
    """
    每分钟限制发2条 2 comments per minutes
    """
    was_limited = getattr(request, 'limited', False)
    if was_limited:
        return JsonResponse({"code": 1, 'msg': 'Comments are too frequent, please try again in 1 minute'})
        pass
    news = get_object_or_404(MyNew, pk = pk)
    print(news)
    form = CommentForm2(data=request.POST)

    if form.is_valid():
        # print('success')
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.nickname = request.user.nickname
        new_comment.avatar = request.user.avatar
        new_comment.news = news
        new_comment.save()

        data = dict()
        data['nickname'] = request.user.nickname
        data['avatar'] = request.user.avatar
        data['timestamp'] = datetime.fromtimestamp(datetime.now().timestamp())
        data['content'] = new_comment.content

        comments = list()
        comments.append(data)

        html = render_to_string(
            "comment/comment_single_news.html", {"comments": comments})

        return JsonResponse({"code":0,"html": html})
    return JsonResponse({"code":1,'msg':'Comment Failed!'})

def get_comments_news(request):
    # if not request.is_ajax():
    #     return HttpResponseBadRequest()
    print(request)
    page = request.GET.get('page')
    page_size = request.GET.get('page_size')
    news_id = request.GET.get('news_id')
    # news = get_object_or_404(MyNew, pk=news_id)
    comments = Comment2.objects.filter(news_id=news_id).order_by('-timestamp').all()
    comment_count = len(comments)

    paginator = Paginator(comments, page_size)
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = []

    if len(rows) > 0:
        code = 0
        html = render_to_string(
            "comment/comment_single_news.html", {"comments": rows})
    else:
        code = 1
        html = ""

    return JsonResponse({
        "code":code,
        "html": html,
        "comment_count": comment_count
    })
