from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Notifications.models import Notification
from AuthUser.models import User
from AuthUser.serializers import UserSerializer

class NotificationSerializer(ModelSerializer):
	actor = UserSerializer(many=False, required=False)
	receiver = UserSerializer(many=False, required=False)

	class Meta:
		model = Notification
		fields = [
			'id',
			'actor',
			'receiver',
			'notification_type',
			'text',
			'read',
			'created_at',
			]
		read_only_fields = ['id', 'created_at']
