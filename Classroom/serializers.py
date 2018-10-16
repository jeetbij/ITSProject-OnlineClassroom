from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Classroom
from AuthUser.models import User
from AuthUser.serializers import UserSerializer

class ClassroomSerializer(ModelSerializer):
	username = serializers.CharField(source='creator.username')
	
	class Meta:
		model = Classroom
		fields = [
			'id',
			'name',
			'code',
			'username',
			'description',
			'image',
			'created_at',
			'is_active'
			]
		read_only_fields = ['id', 'created_at', 'image']


class ClassroomStudentSerializer(ModelSerializer):
	students = UserSerializer(required=True)

	class Meta:
		model = Classroom
		fields = [
			'students'
			]


class ClassroomModeratorSerializer(ModelSerializer):
	moderators = UserSerializer(required=True)

	class Meta:
		model = Classroom
		fields = [
			'moderators'
			]



			