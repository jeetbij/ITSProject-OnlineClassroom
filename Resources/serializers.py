from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Resources.models import Resource
from AuthUser.serializers import UserSerializer
from Classroom.serializers import ClassroomSerializer

class ResourceSerializer(ModelSerializer):
	uploader = UserSerializer(required=False)
	classroom = ClassroomSerializer(required=False, write_only=True)
	classroom_id = serializers.CharField(source='classroom.id')

	class Meta:
		model = Resource
		fields = [
			'id',
			'uploader',
			'classroom_id',
			'classroom',
			'attachment',
			'description',
			'is_lecture',
			'uploaded_on'
			]
		read_only_fields = ['id', 'uploaded_on', 'classroom_id']