"""
Configuration for the Likes app.

Defines the LikesConfig class to configure the Likes application.
"""
from django.apps import AppConfig


class LikesConfig(AppConfig):
    """
    This class configures the 'likes' app and sets up necessary
    settings like the default auto field.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'likes'
