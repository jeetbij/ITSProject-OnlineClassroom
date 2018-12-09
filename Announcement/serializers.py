from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Announcement.models import Announcement
from AuthUser.models import User
from AuthUser.serializers import UserSerializer
from Classroom.serializers import ClassroomSerializer

class AnnouncementSerializer(ModelSerializer):
	announcer = UserSerializer(many=False, required=False)
	classroom = ClassroomSerializer(many=False, required=False, write_only=True)

	class Meta:
		model = Announcement
		fields = [
			'id',
			'content',
			'announcer',
			'classroom',
			'commentCount',
			'created_on',
			]
		read_only_fields = ['id', 'created_on', 'commentCount']