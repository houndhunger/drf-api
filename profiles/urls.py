"""
URL configuration for the 'profiles' app. This includes the routes for
listing profiles and viewing or updating individual profiles.
"""
from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
