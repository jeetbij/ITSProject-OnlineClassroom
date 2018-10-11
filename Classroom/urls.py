from django.conf.urls import url
from .views import ClassroomView, ClassroomStudentView

app_name = 'Classroom'

urlpatterns = [
	url(r'^$', ClassroomView.as_view(), name='classroomview'),
	url(r'^students/$', ClassroomStudentView.as_view(), name='classroomstudentview'),
	]