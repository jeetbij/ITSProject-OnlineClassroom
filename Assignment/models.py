from django.conf import settings
from django.db import models

# Create your models here.

def assignment_upload_path(instance, filename):
	return 'Assignments/{0}'.format(instance.uploader.username, filename)

class Assignment(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="uploaded_assignment")
	attachment = models.FileField(upload_to=assignment_upload_path)
	deadline = models.DateTimeField(null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.uploader.username) + ' -- ' + str(self.title)