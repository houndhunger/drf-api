"""
App configuration for the Followers app.
"""
from django.apps import AppConfig


class FollowersConfig(AppConfig):
    """
    Configuration class for the Followers app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followers'
