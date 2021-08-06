from django.urls import path
from . import views

app_name = 'aboutApp'

urlpatterns = [
    path('lizards/', views.lizards, name='lizards'),  # 企业概况
    path('commentator/', views.commentator, name='commentator'),     # 荣誉资质
]