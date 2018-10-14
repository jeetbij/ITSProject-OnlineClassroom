from django.db import models
from django.conf import settings
from Polls.models import Poll, PollOption

class PollResponse(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="polls")
	poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name="polloption")
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return str(self.poll.poll_text) + ' -- ' + str(self.created_at)