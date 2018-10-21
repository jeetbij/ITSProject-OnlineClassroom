from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Notifications.models import Notification
from AuthUser.models import User
from Notifications.serializers import NotificationSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AuthUser.serializers import UserSerializer
# Create your views here.

class NotificationView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		notification=Notification.objects.filter(receiver=request.user)
		serialized_notification = NotificationSerializer(notification,many=True).data
		return Response(serialized_notification)