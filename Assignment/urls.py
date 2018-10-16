from django.conf.urls import url
from Assignment.views import AssignmentView, SubmissionView, AssignmentCommentView

app_name = 'Assignment'

urlpatterns = [
	url(r'^$', AssignmentView.as_view(), name='assignmentview'),
	url(r'^submission/$', SubmissionView.as_view(), name='submissionview'),
	url(r'^comment/$', AssignmentCommentView.as_view(), name='assignmentcommentview'),
	]