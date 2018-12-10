from django.conf import settings
from django.db import models

# Create your models here.

def userDocumentUploadPath(instance, filename):
	return 'Storage/{0}/{1}'.format(instance.uploader.username, filename)

class UploadDocument(models.Model):
	fileName = models.CharField(max_length=500, null=True, blank=True)
	document = models.FileField(upload_to=userDocumentUploadPath, null=True, blank=True)
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='document_uploader')
	uploaded_on = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.fileName = str(self.document)
		super(UploadDocument, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.fileName) + '->' + str(self.uploaded_on)


class Storage(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_storage')
	allDocuments = models.ManyToManyField(UploadDocument, related_name='user_account')
	limit = models.IntegerField(default=settings.DEFAULT_STORAGE_LIMIT)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user.email) + '->' + str(self.created_date)
