from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from Resources.models import Resource
from Resources.serializers import ResourceSerializer
from Classroom.models import Classroom
from Comment.models import Comment
from Comment.serializers import CommentSerializer
# Create your views here.

class ResourceView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		'''To get all resources in a classroom
		Takes classroom_id, type(lecture OR resource)
		Return all lectures if type is lecture else returns all resources'''

		try:
			classroom = Classroom.objects.get(id=request.GET.get('classroom_id'))
			if request.user.username == classroom.creator.username or request.user in classroom.moderators.all() or request.user in classroom.students.all():
				if request.GET.get('type') == 'lecture':
					resources = Resource.objects.filter(classroom__id=classroom.id, is_lecture=True)
					serializer = ResourceSerializer(resources, many=True)
					return Response(serializer.data)
				elif request.GET.get('type') == 'resource':
					resources = Resource.objects.filter(classroom__id=classroom.id, is_lecture=False)
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
		'''To upload a lecture OR a resource
		Takes classroom_id, is_lecture(True OR False), attachment, description
		Returns newly created object'''

		try:
			print(request.POST, request.data)
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			if request.data.get('is_lecture') == 'True':
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
				print("resource")
				if request.user.username == classroom.creator.username or request.user in classroom.moderators.all() or request.user in classroom.students.all():
					serializer = ResourceSerializer(data=request.data)
					print(request.data)
					if serializer.is_valid():
						serializer.save(uploader=request.user, classroom=classroom)
						return Response(serializer.data)
					else:
						print("error")
						return Response(serializer.errors)
				else:
					return Response({
						"error": "You aren't enrolled in this classroom."
						}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		'''To delete a resource OR lecture
		Takes resource_id
		Returns success if deleted else returns error message'''

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
		'''To get all comments on a resource
		Takes resource_id
		Returns resource with all comments'''

		try:
			resource = Resource.objects.get(id=request.GET.get('resource_id'))
			if request.user.username == resource.classroom.creator or request.user in resource.classroom.moderators.all() or request.user in resource.classroom.students.all():
				allComments = resource.comments.all()
				serialized_comments = CommentSerializer(allComments, many=True).data
				serialized_resource = ResourceSerializer(resource, many=False).data
				serialized_resource['comments'] = serialized_comments
				return Response(serialized_resource)
			else:
				return Response({
					"error": "You can't see this resource."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({
				"error": "Resource query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		'''To post a comment on a resource
		Takes resource_id, comment_id(if replying a comment), content
		Returns resource with all comments'''
		
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
			serialized_comments = CommentSerializer(allComments, many=True).data
			serialized_resource = ResourceSerializer(resource, many=False).data
			serialized_resource['comments'] = serialized_comments
			return Response(serialized_resource)
		except Exception as e:
			return Response({
				"error": "Resource query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)
