"""
Signal handlers for the notifications app, which create notifications
for events such as new posts, likes, comments, and followers.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post
from likes.models import Like
from comments.models import Comment
from followers.models import Follower
from .models import Notification


@receiver(post_save, sender=Post)
def notify_new_post(instance, created, **kwargs):
    """
    Creates a notification for followers when a new post is created.
    """
    if created:
        followers = instance.owner.followed.all()
        for follower in followers:
            Notification.objects.create(
                owner=follower.owner,
                sender=instance.owner,
                notification_type='new_post',
                is_read=False,
                message=(
                    f"{instance.owner.username} created a new post: "
                    f"{instance.title}"
                ),
                post_id=instance
            )


@receiver(post_save, sender=Like)
def notify_new_like(instance, created, **kwargs):
    """
    Creates a notification when a user likes a post.
    """
    if created:
        Notification.objects.create(
            owner=instance.post.owner,
            sender=instance.owner,
            notification_type='like',
            is_read=False,
            message=(
                f"{instance.owner.username} liked your post: "
                f"{instance.post.title}"
            ),
            post_id=instance.post

        )


@receiver(post_save, sender=Follower)
def notify_new_follower(instance, created, **kwargs):
    """
    Creates a notification when a new follower starts following a user.
    """
    if created:
        Notification.objects.create(
            owner=instance.followed,
            sender=instance.owner,
            notification_type='follow',
            is_read=False,
            message=f"{instance.owner.username} started following you."
        )


@receiver(post_save, sender=Comment)
def notify_new_comment(instance, created, **kwargs):
    """
    Creates a notification when a user comments on a post.
    """
    if created:
        Notification.objects.create(
            owner=instance.owner,
            sender=instance.owner,
            notification_type='comment',
            is_read=False,
            message=(
                f"{instance.owner.username} commented on your post: "
                f"{instance.post.title}"
            ),
            post_id=instance.post
        )
