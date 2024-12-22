"""
URL configuration for the Likes app.

Defines URL patterns for listing, creating, retrieving, and deleting likes.
"""
from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
]
