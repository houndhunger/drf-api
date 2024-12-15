from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
        ('post_update', 'Post Update'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
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
    reference_id = models.PositiveIntegerField(null=True, blank=True)  # Reference ID to relate to the post/comment
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"