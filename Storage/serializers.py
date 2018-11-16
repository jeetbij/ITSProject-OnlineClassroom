from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Storage.models import UploadDocument, Storage
from AuthUser.serializers import UserSerializer

class UploadDocumentSerializer(ModelSerializer):

	class Meta:
		model = UploadDocument
		fields = [
			'id',
			'fileName',
			'document',
			'uploaded_on'
			]
		read_only_fields = ['id', 'fileName', 'uploaded_on']


class StorageSerializer(ModelSerializer):
	user = UserSerializer(required=False)
	class Meta:
		model = Storage
		fields = [
			'user',
			'limit',
			'created_date'
			]
		read_only_fields = ['created_date']