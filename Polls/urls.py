from django.conf.urls import url
from Polls.views import PollView

app_name = 'Polls'

urlpatterns = [
	 url(r'^$', PollView.as_view(), name='pollview')
	]