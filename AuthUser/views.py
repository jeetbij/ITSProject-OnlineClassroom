from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class UserView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request, format=None):
		try:
			serializer = UserSerializer(request.user, many=False)
			return Response(serializer.data)
		except:
			return Response('User does not exists.')
		

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		try:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response("serializer is not valid.")
		except Exception as e:
			return Response(e)
