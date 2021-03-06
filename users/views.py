from helpers import AuthorRequiredMixin, get_page_list
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from django.views import generic
from ratelimit.decorators import ratelimit

from .models import Feedback

from .forms import ProfileForm, SignUpForm, UserLoginForm, ChangePwdForm
User = get_user_model()

def login(request):
    if request.method == 'POST':
        next = request.POST.get('next', '')
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['username'] = username
                # return redirect('home')
                return redirect(next)
        else:
            print(form.errors)
    else:
        next = request.GET.get('next', '/home/')
        form = UserLoginForm()
    print(next)
    return render(request, 'registration/login.html', {'form': form, 'next':next})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password1)
            auth_login(request, user)
            request.session['username'] = username
            return redirect('/home/')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/home/')


def change_password(request):
    if request.method == 'POST':
        form = ChangePwdForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.is_staff and not user.is_superuser:
                user.save()
                update_session_auth_hash(request, user)  # ??????session ???????????????
                messages.success(request, '????????????')
                return redirect('users:change_password')
            else:
                messages.warning(request, '???????????????????????????')
                return redirect('users:change_password')
        else:
            print(form.errors)
    else:
        form = ChangePwdForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


class ProfileView(LoginRequiredMixin,AuthorRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        messages.success(self.request, "????????????")
        return reverse('users:profile', kwargs={'pk': self.request.user.pk})



class CollectListView2(generic.ListView):
    model = User
    template_name = 'users/collect_news.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CollectListView2, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_list = get_page_list(paginator, page)
        context['page_list'] = page_list
        return context
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        news = user.collected_news.all()
        return news


class LikeListView2(generic.ListView):
    model = User
    template_name = 'users/like_news.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LikeListView2, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        page_list = get_page_list(paginator, page)
        context['page_list'] = page_list
        return context

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        news = user.liked_news.all()
        return news
