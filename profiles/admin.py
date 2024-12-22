"""
Admin configuration for the Followers app in the admin interface.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
