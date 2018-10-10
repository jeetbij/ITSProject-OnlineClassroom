from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserView(APIView):

	def get(self, request, format=None):
		try:
			username = request.GET.get('username')
			user = User.objects.get(username=username)
		except:
			return Response('User does not exists.')
		serializer = UserSerializer(user, many=False)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		try:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response("serializer is not valid.")
		except Exception as e:
			return Response(e)
