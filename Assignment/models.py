from django.conf import settings
from django.db import models
from Classroom.models import Classroom
from Comment.models import Comment

# Create your models here.

def assignment_upload_path(instance, filename):
	return 'Assignments/{0}'.format(instance.uploader.username, filename)

def submission_upload_path(instance, filename):
	return 'Submission/{0}_{1}'.format(instance.assignment.id, instance.assignment.title, filename)

class Assignment(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="uploaded_assignment")
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True, related_name="assignment")
	attachment = models.FileField(upload_to=assignment_upload_path)
	deadline = models.DateTimeField(null=True, blank=True)
	comments = models.ManyToManyField(Comment, related_name="associated_assignment")
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.uploader.username) + ' -- ' + str(self.title)


class Submission(models.Model):
	submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="assignment_submitter")
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True, related_name="assignment_submission")
	attachment = models.FileField(upload_to=submission_upload_path)
	score = models.IntegerField(default=None, null=True, blank=True)
	submitted_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.submitter.username) + ' -- ' + str(self.assignment.title)