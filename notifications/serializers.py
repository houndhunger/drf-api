from rest_framework import serializers
from .models import Notification
from posts.models import Post  # To access the post's title
from django.contrib.auth.models import User  # To reference User in the sender

class NotificationSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()
    sender_id = serializers.SerializerMethodField()  # Add sender_id field
    post_title = serializers.SerializerMethodField()  # Add a field for post title

    def get_sender_username(self, obj):
        sender = obj.sender # Access the user directly from the notification instance
        return sender.username if sender else None

    def get_sender_id(self, obj):
        sender = obj.sender
        return sender.id if sender else None  # Return the sender's ID if available

    def get_post_title(self, obj):
        if obj.post_id:  # Check if post_id is not null
            post = Post.objects.get(id=obj.post_id.id)  # If obj.post_id is a Post object
            return post.title if post else None
        return None  # Return None if no related post

    class Meta:
        model = Notification
        fields = [
            'id', 'notification_type', 'message', 'created_at', 'is_read',
            'owner', 'sender_username', 'sender_id', 'post_id', 'post_title'
        ]
