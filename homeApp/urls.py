from django.urls import path

from homeApp import views

app_name = 'homeApp'

urlpatterns = [
    path('', views.home, name='home'),                      # 首页
    path('home/', views.home, name='home'),
]