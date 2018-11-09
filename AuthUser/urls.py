from django.conf.urls import url
from .views import UserView, CommonApiView

app_name = 'AuthUser'

urlpatterns = [
	url(r'^user/$', UserView.as_view(), name='userview'),
	url(r'^commonapiview/(?P<token>[\w\-\.]+)', CommonApiView.as_view(), name='commonapiview'),
	]