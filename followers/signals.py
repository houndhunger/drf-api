"""
Signal handlers for the followers app.
This includes notification creation when a user starts following another user.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification
from .models import Follower


@receiver(post_save, sender=Follower)
def notify_new_follower(instance, created, **kwargs):
    """
    Sends a notification when a new follower is created.
    This function is triggered after a Follower instance is saved, and creates
    a notification for the user being followed.
    """
    if created:  # Trigger only when a new follower is created
        Notification.objects.create(
            owner=instance.followed,
            sender=instance.owner,
            notification_type='follow',
            message=f'{instance.owner.username} started following you!'
        )
