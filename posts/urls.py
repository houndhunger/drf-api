"""
URL patterns for handling post-related API endpoints.
Includes endpoints for listing, retrieving, updating, and deleting posts.
"""
from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view())
]
