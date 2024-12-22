"""
Configuration for the 'posts' application. This file defines the settings
and initialization for the posts app in the Django project.
"""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    Configuration class for the 'posts' app. Sets the default auto field
    type to BigAutoField and defines the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
