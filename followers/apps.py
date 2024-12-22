"""
App configuration for the Followers app.
"""
from importlib import import_module
from django.apps import AppConfig


class FollowersConfig(AppConfig):
    """
    Configuration class for the Followers app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followers'

    def ready(self):
        """
        Import signal handlers when the app is ready.
        """
        import_module('followers.signals')
