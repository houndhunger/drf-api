"""
Serializers for the Notification model, including customized fields
such as sender's username, sender's ID, and post title for API responses.
"""
from rest_framework import serializers
from posts.models import Post
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer class for Notification model to customize fields such as
    sender's username, sender's ID, and post title.
    """
    sender_username = serializers.SerializerMethodField()
    sender_id = serializers.SerializerMethodField()
    post_title = serializers.SerializerMethodField()

    def get_sender_username(self, obj):
        """
        Retrieves the username of the sender for the notification.
        """
        sender = obj.sender
        return sender.username if sender else None

    def get_sender_id(self, obj):
        """
        Retrieves the sender's ID for the notification.
        """
        sender = obj.sender
        return sender.id if sender else None

    def get_post_title(self, obj):
        """
        Retrieves the title of the post associated with the notification.
        """
        if obj.post_id:
            post = Post.objects.get(id=obj.post_id.id)
            return post.title if post else None
        return None

    class Meta:
        model = Notification
        fields = [
            'id', 'notification_type', 'message', 'created_at', 'is_read',
            'owner', 'sender_username', 'sender_id', 'post_id', 'post_title'
        ]
