from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from Resources.models import Resource
from Resources.serializers import ResourceSerializer
# Create your views here.

class ResourceView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			classroom = Classroom.objects.get(id=request.GET.get('classroom_id'))
			if request.user.username == classroom.creator.username or request.user in classroom.moderators.all() or request.user in classroom.students.all():
				resources = Resource.objects.filter(classroom__id=classroom.id)
				serializer = ResourceSerializer(resources, many=True)
				return Response(serializer.data)
			else:
				return Response({
					"error": "Your aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		try:
			classroom = Classroom.objects.get(id=request.GET.get('classroom_id'))
			if request.data.get('is_lecture'):
				if request.user.username == classroom.creator.username:
					serializer = ResourceSerializer(data=request.data)
					if serializer.is_valid():
						serializer.save(uploader=request.user, classroom=classroom, is_lecture=True)
						return Response(serializer.data)
					else:
						return Response(serializer.errors)
				else:
					return Response({
						"error": "You aren't authorized to upload lectures in this classroom."
						}, status=status.HTTP_400_BAD_REQUEST)
			else:
				if request.user.username == classroom.creator.username or request.user in classroom.moderators.all() or request.user in classroom.students.all():
					serializer = ResourceSerializer(data=request.data)
					if serializer.is_valid():
						serializer.save(uploader=request.user, classroom=classroom)
						return Response(serializer.data)
					else:
						return Response(serializer.errors)
				else:
					return Response({
						"error": "You aren't enrolled in this classroom."
						}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		try:
			resource = Response.objects.get(id=request.data.get('resource_id'))
			if request.user.username == resource.uploader.username or request.user.username == resource.classroom.creator.username:
				resource.is_deleted=True
				resource.save()
				return Response({
					"success": "Resource successfully deleted."
					}, status=status.HTTP_200_OK)
			else:
				return Response({
					"error": "You can't delete this resource."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Resource query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)


class ResourceCommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			resource = Resource.objects.get(id=request.GET.get('resource_id'))
			if request.user.username == resource.classroom.creator or request.user in resource.classroom.moderators.all() or request.user in resource.classroom.students.all():
				allComments = resource.comments.all()
				serialized_comments = CommentSerializer(allComments, many=True)
				serialized_resource = ResourceSerializer(resource, many=False)
				serialized_resource.data['comments'] = serialized_comments
				return Response(serialized_resource.data)
			else:
				return Response({
					"error": "You can't see this resource."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Resource query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		try:
			resource = Resource.objects.get(id=request.data.get('resource_id'))
			comment = Comment()
			if request.data.get('comment_id'):
				try:
					comment.parent = Comment.objects.get(id=request.data.get('comment_id'))
					comment.commenter = request.user
					comment.comment_text = request.data.get('content')
					comment.save()
				except Exception as e:
					return Response({
						"error": "Comment query doesn't exists."
						}, status=status.HTTP_400_BAD_REQUEST)
			else:
				comment.parent = None
				comment.commenter = request.user
				comment.comment_text = request.data.get('content')
				comment.save()
				resource.comments.add(comment)
				resource.save()
			allComments = resource.comments.all()
			serialized_comments = CommentSerializer(allComments, many=True)
			serialized_resource = ResourceSerializer(resource, many=False)
			serialized_resource.data['comments'] = serialized_comments
			return Response(serialized_resource.data)
		except Exception as e:
			return Response({
				"error": "Resource query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)