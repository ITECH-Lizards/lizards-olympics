from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('<int:pk>/collect_news/', views.CollectListView2.as_view(), name='collect_news'),
    path('<int:pk>/like_news/', views.LikeListView2.as_view(), name='like_news'),
]
