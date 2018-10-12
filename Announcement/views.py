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

from rest_framework import status
# Create your views here.

class AnnouncementView(APIView):

	def get(self, request, format=None):
		classroom_id = request.GET.get('classroom_id')
		announcements = Announcement.objects.filter(classroom__id=classroom_id)
		print(announcements)
		serializer = AnnouncementSerializer(announcements, many=True)
		print("announce")
		return Response(serializer.data)

	def post(self, request, format=None):
		# serializer = AnnouncementSerializer(data=request.data)
		# if serializer.is_valid():
		# 	user = User.objects.get(username=request.data.get('username'))
		# 	classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
		# 	serializer.save(announcer=user, classroom=classroom)
		# 	return Response(serializer.data)
		# else:
		# 	return Response(serializer.errors)
		announcement = Announcement()
		announcement.announcer = User.objects.get(username=request.data.get('username'))
		announcement.content = request.data.get('content')
		announcement.classroom_id = request.data.get('classroom_id')
		announcement.save()
		announcement_serializer = AnnouncementSerializer(announcement, many=False).data
		print(announcement_serializer)
		return Response(announcement_serializer)

	def put(self, request, format=None):
		username = request.data.get('username')
		user = User.objects.get(username=username)
		print(username)
		announcement_id = request.data.get('annoucement_id')
		announcement = Announcement.objects.get(id=announcement_id)
		print(announcement)
		print("announcement.announcer",announcement.announcer)
		print(user)
		if(announcement.announcer==user):
			announcement.content = request.data.get('content')
			announcement.save()
			announcement_serializer = AnnouncementSerializer(announcement, many=False).data
			print(announcement_serializer)
			return Response(announcement_serializer)
		return Response({
				"errors": [
					"You can't update this announcement"
				]
			}, status=status.HTTP_400_BAD_REQUEST)
		
		


class AnnoucementCommentView(APIView):

	def get(self, request, format=None):
		announcement = Announcement.objects.get(id=request.GET.get('id'))
		print("classroom",announcement.classroom)
		announcement_serializer = AnnouncementSerializer(announcement, many=False).data
		print(announcement_serializer)
		allcomments = announcement.comment.all()
		serializedcomments = CommentSerializer(allcomments, many=True)
		announcement_serializer['comments'] = serializedcomments.data
		serializedclassroom = ClassroomSerializer(announcement.classroom, many=False)
		announcement_serializer['classroom'] = serializedclassroom.data
		return Response(announcement_serializer)

	def post(self, request, format=None):
		comment = Comment()
		comment.comment_text = request.data.get('comment_text')
		comment.commenter = User.objects.get(username=request.data.get('commenter'))
		comment.parent = Comment.objects.get(id=request.data.get('parrent_comment_id'))
		comment.save()
		print(comment)
		announcement = Announcement.objects.get(id=request.data.get('announcement_id'))
		announcement.comment.add(comment)
		announcement.save()
		print(announcement)
		allcomments = announcement.comment.all()
		serialized_announcement = AnnouncementSerializer(announcement,many=False).data
		serialized_comment = CommentSerializer(allcomments,many=True).data
		serialized_classroom = ClassroomSerializer(announcement.classroom,many=False).data
		serialized_announcement['comments'] = serialized_comment
		serialized_announcement['classroom'] = serialized_classroom
		return Response(serialized_announcement)

	




