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
import threading
# Create your views here.

class NotificationView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			notification=Notification.objects.filter(receiver=request.user)
			serialized_notification = NotificationSerializer(notification,many=True).data
			return Response(serialized_notification)
		except Exception as e:
			return Response({
				"error": "Something went wrong."
				}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, format=None):
		try:
			notification = Notification.objects.get(id=request.GET.get('notification_id'))
			notification.read = True
			notification.save()
			serialized_notification = NotificationSerializer(notification, many=False).data
			return Response(serialized_notification)
		except Exception as e:
			print (e)
			return Response({
				"error": "Notification doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)



def saveNotification(sender, receiver, text, type):
	try:
		notification = Notification()
		notification.actor = sender
		notification.receiver = receiver
		notification.text = text
		notification.notification_type = type
		notification.save()
	except:
		pass

def Notify(sender, text, type, receiver=None):
	for re in receiver:
		thread_process = threading.Thread(target=saveNotification, kwargs={
				"sender":sender,
				"receiver":re,
				"text":text,
				"type": type
			})
		thread_process.start()
	return True