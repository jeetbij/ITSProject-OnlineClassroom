from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Comment.models import Comment
from AuthUser.models import User
from Comment.serializers import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class CommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			comment = Comment.objects.get(id=request.GET.get('id'))
			child_comments = comment.child_comment.all()
			serialized_comments = CommentSerializer(child_comments, many=True).data
			serializer = CommentSerializer(comment, many=False).data
			serializer['child'] = serialized_comments
			return Response(serializer)
		except Exception as e:
			return Response({
				"error": "Comment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(commenter=request.user)
			return Response(serializer.data)
		return Response(serializer.errors)