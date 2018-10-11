from django.conf.urls import url
from Assignment.views import AssignmentView

app_name = 'Assignment'

urlpatterns = [
	url(r'^$', AssignmentView.as_view(), name='assignmentview')
	]