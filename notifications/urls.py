from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('notifications/<int:notification_id>/mark-read/', views.NotificationMarkReadView.as_view(), name='mark-notification-read'),
    path('notifications/mark_all_read/', views.NotificationMarkAllReadView.as_view(), name='mark_all_notifications_read'),  
    path('notifications/delete_all_read/', views.NotificationDeleteAllReadView.as_view(), name='delete_all_read_notifications'),
]