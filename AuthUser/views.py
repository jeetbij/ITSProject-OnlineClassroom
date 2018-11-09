from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
import requests
from rest_framework_jwt.settings import api_settings
from django.conf import settings

class UserView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request, format=None):
		'''To get user profile
		returns the user object'''

		try:
			serializer = UserSerializer(request.user, many=False)
			return Response(serializer.data)
		except:
			return Response('User does not exists.')
		
	def post(self, request, format=None):
		'''To register user profile
		returns the user object'''
		serializer = UserSerializer(data=request.data)
		try:
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response("serializer is not valid.")
		except Exception as e:
			return Response(e)


class CommonApiView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request, token, format=None):
		clientSecret =  "d22a0e57432d7e2c9e8cd3f2d219588ab5a31d13451a4cfa4d6ce0cba8b28b9a702f3b28d6f80f1a39708dcea9dd623ba9f48325dc314d05ed9980bc690b92d0"

		detailUrl = "https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
		response = requests.post(url=detailUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'token': token, 'secret':clientSecret})
		try:
			data = eval(str(response.json()['student'][0]))
			username = data['Student_ID']
			first_name = data['Student_First_Name']
			last_name = data['Student_Last_name']
			email = data['Student_Email']
			mobileNo = data['Student_Mobile']

			jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
			jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

			try:
				user = User.objects.get(username=username)
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				return HttpResponseRedirect(settings.REDIRECT_URL+'/#/login?token='+str(token))

			except:
				user = User()
				user.username = username
				user.first_name = first_name
				user.last_name = last_name
				user.email = email
				user.mobile_no = mobileNo
				user.set_password("iamstudent")
				user.save()

				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)

				return HttpResponseRedirect(settings.REDIRECT_URL+'/#/login?token='+str(token))
		except Exception as e:
			print(e)
			return HttpResponse("Common Api error")

		
		return HttpResponse(response.text)