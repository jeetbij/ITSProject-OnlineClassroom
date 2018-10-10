from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Classroom
from .serializers import ClassroomSerializer
# Create your views here.

class ClassroomView(APIView):

	def get(self, request, format=None):
		classroom_id = request.GET.get('classroom_id')
		classroom = Classroom.objects.get(id=classroom_id)
		print(classroom)
		serializer = ClassroomSerializer(classroom, many=False)
		print(serializer.data)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ClassroomSerializer(data=request.data)
		print (serializer)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response("serializer is not valid.")