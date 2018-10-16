from django.conf.urls import url
from Resources.views import ResourceView, ResourceCommentView

app_name = 'Resources'

urlpatterns = [
	url(r'^$', ResourceView.as_view(), name='resourceview'),
	url(r'^comment/$', ResourceCommentView.as_view(), name='resourcecommentview'),
	]