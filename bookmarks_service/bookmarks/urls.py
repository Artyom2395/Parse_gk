from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bookmarks/', views.add_bookmark, name='bookmark_list'),
    path('bookmarks/list', views.bookmark_list, name='bookmarks_list'),
    path('login/', auth_views.LoginView.as_view(template_name = "bookmarks/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "bookmarks/logout.html"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
