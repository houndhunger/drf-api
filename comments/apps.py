"""
Configuration for the 'comments' app in the Django project.
This file configures the app's settings such as the default auto field type.
"""
from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """
    Configuration for the 'comments' app. 
    Sets the default auto field and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
