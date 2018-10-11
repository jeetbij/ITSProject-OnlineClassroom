from django.conf.urls import url
from .views import ClassroomView

app_name = 'Classroom'

urlpatterns = [
	url(r'^$', ClassroomView.as_view(), name='classroomview'),
	]