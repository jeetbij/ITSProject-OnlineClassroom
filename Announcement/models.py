from django.conf import settings
from django.db import models
from Comment.models import Comment

# Create your models here.

class Announcement(models.Model):
	announcer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcer_user')
	content = models.TextField(null=True)
	# comment = models.OneToOneField(Comment, on_delete=models.SET_NULL, null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.announcer) + ' -- ' + str(self.created_on)