from django.conf.urls import url
from .views import UserView

app_name = 'AuthUser'

urlpatterns = [
	url(r'^user/', UserView.as_view(), name='userview'),
	]