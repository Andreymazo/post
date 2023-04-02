from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from users import views



urlpatterns = [
    path('', views.PostList.as_view()),
    path('register/', views.UserRegistration.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    re_path(r'rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)