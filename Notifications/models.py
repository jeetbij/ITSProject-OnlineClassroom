from django.conf import settings
from django.db import models

# Create your models here.

class Notification(models.Model):
	actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actor")
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
	text = models.CharField(max_length=2000, null=True, blank=True)

	C = 'Classroom'
	AN = 'Announcement'
	AS = 'Assignment'
	R = 'Resources'
	P = 'Poll'
	CR = 'CommentReply'

	NOTIFICATION_TYPE =(
		(C, 'Classroom'),
		(AN, 'Announcement'),
		(AS, 'Assignment'),
		(R, 'Resources'),
		(P, 'Poll'),
		(CR, 'CommentReply')
	)

	notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE, default='C')				
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	read = models.BooleanField(default=False)

	def __str__(self):
		return str(self.actor.username) + ' -- ' +str(self.receiver.username) + ' -- ' + str(self.created_at)
