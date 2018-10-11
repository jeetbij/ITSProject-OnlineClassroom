from django.conf.urls import url
from Announcement.views import AnnouncementView

app_name = 'Announcement'
urlpatterns = [
	url(r'', AnnouncementView.as_view(), name='announcementview')
	]