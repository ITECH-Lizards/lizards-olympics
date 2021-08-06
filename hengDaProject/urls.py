"""hengDaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from homeApp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),                  # 管理员
    path('', home, name='home'),                      # 首页
    path('home/', home, name='home'),
    path('aboutApp/', include('aboutApp.urls')),      # 公司简介
    path('contactApp/', include('contactApp.urls')),  # 人才招聘
    path('newsApp/', include('newsApp.urls')),        # 新闻动态
    path('ueditor/',include('DjangoUeditor.urls' )),  # 富文本应用
    path('search/', include('haystack.urls')),        # 搜索应用
    path('comment/', include('comment.urls')),
    path('users/', include('users.urls')),
    path('github/', include('social_django.urls', namespace='social')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
