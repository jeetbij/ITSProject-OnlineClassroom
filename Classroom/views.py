from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Classroom
from .serializers import ClassroomSerializer
from AuthUser.serializers import UserSerializer
from AuthUser.models import User
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


class ClassroomStudentView(APIView):

	def get(self, request, format=None):
		classroom = Classroom.objects.get(id=request.GET.get('id'))
		students = classroom.students.all()
		serialized_students = UserSerializer(students, many=True).data

		return Response(serialized_students)

	def post(self, request, format=None):
		classroom = Classroom.objects.get(id=request.data.get('id'))
		student_ids = request.data.get('students')
		student_users = [User.objects.get(username=student_id) for student_id in student_ids]
		classroom.students.add(*student_users)
		classroom.save()
		serialized_classroom = ClassroomSerializer(classroom, many=False).data
		serialized_students = UserSerializer(classroom.students.all(), many=True).data
		serialized_classroom['students'] = serialized_students

		return Response(serialized_classroom)