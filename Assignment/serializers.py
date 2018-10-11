from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Assignment.models import Assignment
from AuthUser.models import User
from AuthUser.serializers import UserSerializer

class AssignmentSerializer(ModelSerializer):
	uploader = UserSerializer(required=False)

	class Meta:
		model = Assignment
		fields = [
			'id',
			'title',
			'uploader',
			'attachment',
			# 'deadline',
			'created_on'
			]
		read_only_fields = ['id', 'created_on']