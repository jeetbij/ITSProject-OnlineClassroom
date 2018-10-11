from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Comment.models import Comment
from AuthUser.models import User
from AuthUser.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
	commenter = UserSerializer(many=False, required=False)
	
	class Meta:
		model = Comment
		fields = [
			'id',
			'comment_text',
			'commenter',
			'created_at',
			]
		read_only_fields = ['id', 'created_at', 'commenter']