from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Announcement.models import Announcement

from Announcement.serializers import AnnouncementSerializer
from AuthUser.models import User
from Classroom.models import Classroom
from Comment.serializers import CommentSerializer

# Create your views here.

class AnnouncementView(APIView):

	def get(self, request, format=None):
		announcements = Announcement.objects.filter(classroom__id=request.GET.get('classroom_id'))
		serializer = AnnouncementSerializer(announcements, many=True)
		print("announce")
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = AnnouncementSerializer(data=request.data)
		if serializer.is_valid():
			user = User.objects.get(username=request.data.get('username'))
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			serializer.save(announcer=user, classroom=classroom)
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class AnnoucementCommentView(APIView):

	def get(self, request, format=None):
		announcement = Announcement.objects.get(id=request.GET.get('id'))
		announcement_serializer = AnnouncementSerializer(announcement, many=False).data
		allcomments = announcement.comment.all()
		serializedcomments = CommentSerializer(allcomments, many=True)
		announcement_serializer['comments'] = serializedcomments.data
		
		return Response(announcement_serializer)