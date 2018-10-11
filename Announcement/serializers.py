from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Announcement.models import Announcement
from AuthUser.models import User

class AnnouncementSerializer(ModelSerializer):
	username = serializers.CharField(source='announcer.username')

	class Meta:
		model = Announcement
		fields = [
			'id',
			'content',
			'username',
			'created_on',
			]
		read_only_fields = ['id', 'created_on']