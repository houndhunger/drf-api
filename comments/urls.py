"""
URL patterns for comment-related views, including listing all comments,
creating a new comment, and managing individual comments by id (retrieve,
update, or delete).
"""
from django.urls import path
from comments import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view())
]
