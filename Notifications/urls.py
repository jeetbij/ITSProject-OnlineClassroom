from django.conf.urls import url
from Notifications.views import NotificationView

app_name = 'Notifications'

urlpatterns = [
	url(r'^$', NotificationView.as_view(), name='notification_view')
	]