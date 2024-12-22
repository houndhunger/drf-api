"""
Django app configuration for the 'profiles' app.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' app.
    Sets the default auto field and the app's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
