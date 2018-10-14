from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from PollResponse.models import PollResponse
from AuthUser.models import User
from AuthUser.serializers import UserSerializer
from Polls.serializers import PollSerializer, PollOptionSerializer

class PollResponseSerializer(ModelSerializer):
	user = UserSerializer(many=False, required=False)
	poll_option = PollOptionSerializer(many=False, required=False)
	# poll = PollSerializer(many=False, required=False)
	class Meta:
		model = PollResponse
		fields = [
			'id',
			'user',
			# 'poll',
			'poll_option',
			'created_at',
			]
		read_only_fields = ['id', 'created_at']
