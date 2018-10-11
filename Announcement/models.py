from django.conf import settings
from django.db import models
from Comment.models import Comment
from Classroom.models import Classroom

# Create your models here.

class Announcement(models.Model):
	announcer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcer_user')
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='class_announcement')
	content = models.TextField(null=True)
	comment = models.ManyToManyField(Comment, related_name="announcement")
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.announcer) + ' -- ' + str(self.created_on)