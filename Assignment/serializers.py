from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Assignment.models import Assignment, Submission
from AuthUser.models import User
from AuthUser.serializers import UserSerializer
from Classroom.serializers import ClassroomSerializer

class AssignmentSerializer(ModelSerializer):
	uploader = UserSerializer(required=False)
	classroom = ClassroomSerializer(required=False, write_only=True)
	class Meta:
		model = Assignment
		fields = [
			'id',
			'title',
			'uploader',
			'classroom',
			'attachment',
			'max_score',
			'deadline',
			'created_on'
			]
		read_only_fields = ['id', 'created_on']


class SubmissionSerializer(ModelSerializer):
	submitter = UserSerializer(required=False)
	assignment_id = serializers.CharField(source='assignment.id')
	class Meta:
		model = Submission
		fields = [
			'id',
			'submitter',
			'assignment_id',
			'attachment',
			'submitted_on'
			]

		read_only_fields = ['id', 'assignment_id', 'submitted_on']