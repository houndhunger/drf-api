from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
        ('post_update', 'Post Update'),
        ('new_post', 'New Post'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_notifications',
        null=True,  # Allow null sender
    )
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPES, default='post_update'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    
    post_id = models.ForeignKey(
        Post,  # Use the correct model reference
        related_name='notifications', 
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"Notification for {self.owner.username}: {self.message}"