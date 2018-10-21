from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Announcement.models import Announcement

from Announcement.serializers import AnnouncementSerializer
from AuthUser.models import User
from Classroom.models import Classroom
from Comment.serializers import CommentSerializer
from Classroom.serializers import ClassroomSerializer
from Comment.models import Comment

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class AnnouncementView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		classroom_id = request.GET.get('classroom_id')
		try:
			announcements = Announcement.objects.filter(classroom__id=classroom_id)
			serializer = AnnouncementSerializer(announcements, many=True)
			return Response(serializer.data)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		try:
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			if request.user.username == classroom.creator.username:
				serializer = AnnouncementSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save(announcer=request.user, classroom=classroom)
					return Response(serializer.data)
				else:
					return Response(serializer.errors)
			else:
				return Response({
					"error": "You aren't authorized to add data in this classroom."
					}, status = status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, format=None):
		try:
			announcement_id = request.data.get('annoucement_id')
			announcement = Announcement.objects.get(id=announcement_id)
			if request.user.username == announcement.announcer.username:
				announcement.content = request.data.get('content')
				announcement.save()
				announcement_serializer = AnnouncementSerializer(announcement, many=False).data
				return Response(announcement_serializer)
			return Response({
					"errors": [
						"You can't update this announcement"
					]
				}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "You are not authorized to make changes in this classroom."
				}, status=status.HTTP_400_BAD_REQUEST)


class AnnoucementCommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			announcement = Announcement.objects.get(id=request.GET.get('id'))
			if request.user.username == announcement.classroom.creator.username or request.user in announcement.classroom.moderators.all() or request.user in announcement.classroom.students.all():
				announcement_serializer = AnnouncementSerializer(announcement, many=False).data
				allcomments = announcement.comment.all()
				print("Start")
				comments_serialized=[]
				for comment in allcomments:
					serializedcomment = CommentSerializer(comment, many=False).data
					 
					serializedcomment['has_Upvoted']='1'
					serializedcomment['has_Downvoted']='1'
					print(serializedcomment)
					comments_serialized.append(serializedcomment)
				# serializedcomments = CommentSerializer(allcomments, many=True)
				announcement_serializer['comments'] = comments_serialized
				serializedclassroom = ClassroomSerializer(announcement.classroom, many=False)
				announcement_serializer['classroom'] = serializedclassroom.data
				return Response(announcement_serializer)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Announcement query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		announcement_id = request.data.get('announcement_id')
		try:
			announcement = Announcement.objects.get(id=announcement_id)
			if request.user.username == announcement.classroom.creator.username or request.user in announcement.classroom.moderators.all() or request.user in announcement.classroom.students.all():
				comment = Comment()
				if request.data.get('comment_id'):
					try:
						comment.parent = Comment.objects.get(id=request.data.get('comment_id'))
						comment.commenter = request.user
						comment.comment_text = request.data.get('comment')
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
					announcement.comment.add(comment)
					announcement.save()
				allComments = announcement.comment.all()
				serialized_comments = CommentSerializer(allComments, many=True)
				serialized_announcement = AnnouncementSerializer(announcement, many=False)
				serialized_announcement.data['comments'] = serialized_comments
				return Response(serialized_announcement.data)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Announcement query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)





