from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Comment.models import Comment
from AuthUser.models import User
from Comment.serializers import CommentSerializer
# Create your views here.

class CommentView(APIView):

	def get(self, request, format=None):
		comments = Comment.objects.all()
		serializer = CommentSerializer(comments, many=True)

		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			comment = Comment()
			comment.commenter = User.objects.get(username=serializer.validated_data.pop('commenter')['username'])
			comment.comment_text = serializer.validated_data.pop('comment_text')
			comment.save()
		return Response(CommentSerializer(comment, many=False).data)