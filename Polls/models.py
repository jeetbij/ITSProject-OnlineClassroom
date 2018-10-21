from django.db import models
from django.conf import settings
from Classroom.models import Classroom
# Create your models here.

class Poll(models.Model):
	creater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='class_poll', null=True, blank=True)
	poll_text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return str(self.creater)+' -- '+  str(self.poll_text)+ ' -- ' + str(self.created_at)

class PollOption(models.Model):
	parrent_poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	option_text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return str(self.option_text) + ' -- ' + str(self.created_at)

# class PollResponse(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# 	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll")
# 	poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name="poll_option")
# 	created_at = models.DateTimeField(auto_now_add=True, blank=True)
# 	def __str__(self):
# 		return str(self.poll_option.option_text) + ' -- ' + str(self.created_at)