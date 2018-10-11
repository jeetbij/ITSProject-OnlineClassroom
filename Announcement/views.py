from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Announcement.models import Announcement

from Announcement.serializers import AnnouncementSerializer
from AuthUser.models import User

# Create your views here.

class AnnouncementView(APIView):

	def get(self, request, format=None):
		announcements = Announcement.objects.all()
		serializer = AnnouncementSerializer(announcements, many=True)

		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = AnnouncementSerializer(data=request.data)
		if serializer.is_valid():
			user = User.objects.get(username=request.data.get('username'))
			serializer.save(announcer=user)
			return Response(serializer.data)
		else:
			return Response(serializer.errors)