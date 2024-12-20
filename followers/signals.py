from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Follower  # Assuming your follower model is in models.py
from notifications.models import Notification  # Adjust import according to your Notification model

@receiver(post_save, sender=Follower)
def notify_new_follower(sender, instance, created, **kwargs):
    if created:  # Trigger only when a new follower is created
        # Create a notification (adjust fields as per your model)
         Notification.objects.create(
            owner=instance.followed,  # The user being followed
            sender=instance.owner,  # The user who is following
            notification_type='follow',  # Set the type to 'follow'
            message=f'{instance.owner.username} started following you!'  # Customize message
        )
