from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Classroom
from AuthUser.models import User

class ClassroomSerializer(ModelSerializer):
	username = serializers.CharField(source='creator.username')
	
	class Meta:
		model = Classroom
		fields = [
			'id',
			'name',
			'username',
			'created_at'
			]
		read_only_fields = ['id', 'created_at']

	def create(self, validated_data):
		name = validated_data.pop('name')
		username = validated_data.pop('creator')['username']
		classroom = Classroom()
		classroom.name = name
		classroom.creator = User.objects.get(username=username)
		classroom.save()
		return (classroom)