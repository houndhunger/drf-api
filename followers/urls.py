"""
URL patterns for follower-related views, including listing followers and 
following/unfollowing users.
"""
from django.urls import path
from followers import views


urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view())
]
