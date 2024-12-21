from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Notification
from posts.models import Post
from likes.models import Like
from comments.models import Comment
from followers.models import Follower

# Notification for new post creation
@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):
    if created:
        # Notify all followers of the post's owner
        followers = instance.owner.followed.all()
        for follower in followers:
            Notification.objects.create(
                owner=follower.owner,
                sender=instance.owner,
                notification_type='new_post',
                is_read=False,
                message=f"{instance.owner.username} created a new post: {instance.title}",
                post_id=instance
            )

# Notification for likes
@receiver(post_save, sender=Like)
def notify_new_like(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            owner=instance.post.owner,  # Assuming post has a 'user' field for the owner
            sender=instance.owner,  # The user who liked the post
            notification_type='like',
            is_read=False,
            message=f"{instance.owner.username} liked your post: {instance.post.title}",
            post_id=instance.post

        )

# Notification for new followers
@receiver(post_save, sender=Follower)
def notify_new_follower(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            owner=instance.followed,
            sender=instance.owner,  # The user who is following
            notification_type='follow',
            is_read=False,
            message=f"{instance.owner.username} started following you."
        )

# Notification for new comments
@receiver(post_save, sender=Comment)
def notify_new_comment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            owner=instance.owner,
            sender=instance.owner,  # Comment owner as sender
            notification_type='comment',
            is_read=False,
            message=f"{instance.owner.username} commented on your post: {instance.post.title}",
            post_id=instance.post
        )