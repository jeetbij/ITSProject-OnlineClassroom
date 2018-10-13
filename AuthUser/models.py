from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def image_upload_path(instance, filename):
	return "Profile/{0}".format(instance.user.username, filename)

class User(AbstractUser):
	mobile_no = models.CharField(max_length=100)
	is_faculty = models.BooleanField(default=False)
	avatar = models.ImageField(upload_to=image_upload_path, default='default_avatar.png')

	def __str__(self):
		return str(self.username)