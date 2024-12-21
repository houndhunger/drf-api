from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    """
    List all notifications for the logged-in user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(owner=self.request.user)

class NotificationUpdate(generics.UpdateAPIView):
    """
    Mark a notification as read when clicked.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        notification = self.get_object()  # Get the notification from the URL parameter
        # Ensure the notification belongs to the logged-in user
        if notification.owner != self.request.user:
            raise NotFound("Notification not found or does not belong to the logged-in user.")
        # Mark as read
        serializer.save(is_read=True)
    
    def get_object(self):
        """
        Override to ensure we fetch the correct notification based on URL parameter.
        """
        obj = super().get_object()
        obj.is_read = True  # Mark as read
        obj.save()  # Save the updated notification
        return obj

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

class NotificationMarkReadView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated

    def post(self, request, notification_id, *args, **kwargs):
        """
        Marks a specific notification as read for the authenticated user.
        """
        try:
            # Retrieve the notification for the authenticated user by its ID
            notification = Notification.objects.get(id=notification_id, owner=request.user)
            # Mark the notification as read
            notification.is_read = True
            notification.save()
            return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"detail": "Notification not found or not owned by the user."}, status=status.HTTP_404_NOT_FOUND)

class NotificationMarkUnreadView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated

    def post(self, request, notification_id, *args, **kwargs):
        """
        Marks a specific notification as unread for the authenticated user.
        """
        try:
            # Retrieve the notification for the authenticated user by its ID
            notification = Notification.objects.get(id=notification_id, owner=request.user)
            # Mark the notification as unread
            notification.is_read = False
            notification.save()
            return Response({"detail": "Notification marked as unread."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"detail": "Notification not found or not owned by the user."}, status=status.HTTP_404_NOT_FOUND)

class NotificationMarkAllReadView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated

    def post(self, request, *args, **kwargs):
        # Retrieve notifications for the authenticated user that are not read
        notifications = Notification.objects.filter(owner=request.user, is_read=False)

        if notifications.exists():
            notifications.update(is_read=True)  # Mark them as read
            return Response({"detail": "All notifications marked as read."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No unread notifications found."}, status=status.HTTP_404_NOT_FOUND)

class NotificationDeleteAllReadView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # Delete all notifications marked as read for the logged-in user
        notifications = Notification.objects.filter(owner=request.user, is_read=True)
        if notifications.exists():
            notifications.delete()  # Delete read notifications
            return Response({"detail": "All read notifications deleted."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No read notifications found."}, status=status.HTTP_404_NOT_FOUND)
