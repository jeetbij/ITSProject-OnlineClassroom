from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Polls.models import Poll, PollOption, PollResponse
from AuthUser.models import User
from AuthUser.serializers import UserSerializer
from Classroom.serializers import ClassroomSerializer


class PollSerializer(ModelSerializer):
	creater = UserSerializer(many=False, required=True)
	classroom = ClassroomSerializer(many=False,required=False)
	class Meta:
		model = Poll
		fields = [
			'id',
			'creater',
			'classroom',
			'poll_text',
			'created_at'
			]
		read_only_fields = ['id', 'created_at']

class PollOptionSerializer(ModelSerializer):
	# parrent_poll = PollSerializer(many=False, required=False)
	class Meta:
		model = PollOption
		fields = [
			'id',
			'option_text',
			'created_at',
			]
		read_only_fields = ['id', 'created_at']

class PollResponseSerializer(ModelSerializer):
	user = UserSerializer(many=False, required=False)
	poll_option = PollOptionSerializer(many=False, required=False)
	class Meta:
		model = PollResponse
		fields = [
			'id',
			'user',
			'poll_option',
			'created_at',
			]
		read_only_fields = ['id', 'created_at']




