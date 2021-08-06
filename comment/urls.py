from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path('submit_comment_news/<int:pk>',views.submit_comment_news, name='submit_comment_news'),
    path('get_comments_news/', views.get_comments_news, name='get_comments_news'),
]