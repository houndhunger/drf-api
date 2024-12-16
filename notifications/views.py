from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    """
    List all notifications for the logged-in user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationUpdate(generics.UpdateAPIView):
    """
    Mark a notification as read.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        notification = self.get_object()  # Get the notification from the URL parameter
        # Ensure the notification belongs to the logged-in user
        if notification.user != self.request.user:
            raise NotFound("Notification not found or does not belong to the logged-in user.")
        # Mark as read
        serializer.save(is_read=True)

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a notification and delete it if the user is the owner.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Notification.objects.all()

    def perform_destroy(self, instance):
        # You could add any custom logic here if needed before deleting
        instance.delete()
