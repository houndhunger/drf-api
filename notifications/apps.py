"""
App configuration for the notifications app. This is where signals
and other app-specific setup can be initialized.
"""
from importlib import import_module
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """
    Configuration class for the notifications app.
    This includes setup of app signals.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        """
        Import signals to initialize the app's notification system.
        """
        import_module('notifications.signals')
