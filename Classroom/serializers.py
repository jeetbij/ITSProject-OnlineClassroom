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
			'username',
			'created_at',
			'is_active'
			]
		read_only_fields = ['id', 'created_at']

	# def create(self, validated_data):
	# 	name = validated_data.pop('name')
	# 	username = validated_data.pop('creator')['username']
	# 	classroom = Classroom()
	# 	classroom.name = name
	# 	classroom.creator = User.objects.get(username=username)
	# 	classroom.save()
	# 	return (classroom)

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



			