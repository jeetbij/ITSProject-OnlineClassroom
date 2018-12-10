from django.conf import settings
from django.db import models
from Classroom.models import Classroom
from Comment.models import Comment

# Create your models here.

def upload_resource_path(instance, filename):
	return 'Resources/{0}_{1}/{2}/{3}'.format(instance.classroom.id, instance.classroom.name, instance.uploader.username, filename)

class Resource(models.Model):
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaderResource')
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroomResource')
	attachment = models.FileField(upload_to=upload_resource_path, null=True, blank=True)
	description = models.CharField(max_length=300, null=True, blank=True)
	comments = models.ManyToManyField(Comment, related_name='commentResource')
	uploaded_on = models.DateTimeField(auto_now_add=True)
	is_lecture = models.BooleanField(default=False)
	is_deleted = models.BooleanField(default=False)

	def __str__(self):
		return str(self.uploader.username) + ' -- ' + str(self.uploaded_on) + ' -- ' + str(self.is_deleted)