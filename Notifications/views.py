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
import sendgrid
from sendgrid.helpers.mail import *
# Create your views here.

SENDGRID_APIKEY = "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"

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
			if request.user == notification.receiver:
				notification.read = True
				notification.save()
				serialized_notification = NotificationSerializer(notification, many=False).data
				return Response(serialized_notification)
			else:
				return Response({
				"error": "You are not authorized to change this notification."
				}, status=status.HTTP_400_BAD_REQUEST)
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
		print(notification)
		notification.save()
	except Exception as e:
		print(e)

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


def mail(recipient, subject, body):
	sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_APIKEY)
	from_email = Email("chandrajeet.c16@iiits.in")
	to_email = Email(recipient)
	subject = subject
	content = Content("text/plain", body)
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	# print(response.status_code)
	# print(response.body)
	# print(response.headers)

def sendMail(recipient, subject, body):
	for re in recipient:
		thread_process = threading.Thread(target=mail, kwargs={
				"recipient":re,
				"subject":subject,
				"body":body
			})
		thread_process.start()
	return True
