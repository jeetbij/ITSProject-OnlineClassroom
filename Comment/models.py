from django.conf import settings
from django.db import models

# Create your models here.

class Comment(models.Model):
	parent = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True, related_name="parent_comment")
	commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	comment_text = models.TextField()
	upvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='all_upvoters')
	downvoters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="all_downvoters")
	created_at = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return str(self.commenter.username) + ' -- ' + str(self.created_at)