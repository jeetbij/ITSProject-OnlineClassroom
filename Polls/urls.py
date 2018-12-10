from django.conf.urls import url
from Polls.views import PollView, PollDetail

app_name = 'Polls'

urlpatterns = [
	 url(r'^$', PollView.as_view(), name='pollview'),
	 url(r'^polldetail/$', PollDetail.as_view(), name='polldetail')
	]