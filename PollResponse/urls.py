from django.conf.urls import url
from PollResponse.views import PollResponseView

app_name = 'PollResponse'

urlpatterns = [
	 url(r'^$', PollResponseView.as_view(), name='poll_response_view')
	]