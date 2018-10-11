from django.conf.urls import url
from Announcement.views import AnnouncementView, AnnoucementCommentView

app_name = 'Announcement'
urlpatterns = [
	url(r'^$', AnnouncementView.as_view(), name='announcementview'),
	url(r'^comment/$', AnnoucementCommentView.as_view(), name='announcementcommentview')
	]