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
		comment = Comment.objects.get(id=request.GET.get('id'))
		child_comments = comment.child_comment.all()
		serialized_comments = CommentSerializer(child_comments, many=True).data
		serializer = CommentSerializer(comment, many=False).data
		serializer['child'] = serialized_comments
		return Response(serializer)

	def post(self, request, format=None):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			user = User.objects.get(username=request.data.get('username'))
			serializer.save(commenter=user)
		return Response(serializer.data)