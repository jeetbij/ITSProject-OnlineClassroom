from rest_framework.views import APIView


from .models import Classroom
from .serializers import ClassroomSerializer
from AuthUser.serializers import UserSerializer
from AuthUser.models import User

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.
from rest_framework import status	

class ClassroomView(APIView):
	def get(self, request, format=None):
		# classroom_id = request.GET.get('classroom_id')
		classroom = Classroom.objects.all()
		print(classroom)
		serializer = ClassroomSerializer(classroom, many=True)
		print(serializer.data)
		return Response(serializer.data)

	def post(self, request, format=None):
		classroom_name = request.data.get('name')
		classroom_creator = request.data.get('username')
		classroom = Classroom()
		print(classroom_name, classroom_creator)
		classroom.name = classroom_name
		classroom.creator = User.objects.get(username=classroom_creator)
		classroom.save()
		serialized_classroom = ClassroomSerializer(classroom, many=False)
		print(serialized_classroom.data)
		return Response(serialized_classroom.data)
		# print(request.data)
		# serializer = ClassroomSerializer(data=request.data)
		# print (serializer)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	# classroom = Classroom()
		# 	# classroom.name = serializer.data.name
		# 	# classroom.creator = User.objects.get(username=serializer.data.username)
		# 	# classroom.save()
		# 	print("serializer.data",serializer.data)
		# 	return Response(serializer.data)
		# else:
		# 	return Response("serializer is not valid.")

	def put(self, request, format=None):
		classroom_creator = request.data.get('username')
		classroom_name = request.data.get('name')
		classroom_id = request.data.get('id')
		classroom_isActive = request.data.get('isActive')
		user = User.objects.get(username=classroom_creator)
		classroom = Classroom.objects.get(id=classroom_id)
		if(classroom.creator==user):
			classroom.name=classroom_name
			classroom.is_active=classroom_isActive
			classroom.save()
			classroom_serializer=ClassroomSerializer(classroom,many=False).data
			return Response(classroom_serializer)
		return Response({
				"errors": [
					"You can't update this classroom"
				]
			}, status=status.HTTP_400_BAD_REQUEST)


class ClassroomStudentView(APIView):
	def get(self, request, format=None):
		classroom_id = request.GET.get('id')
		classroom = Classroom.objects.get(id=classroom_id)
		print(classroom)
		students = classroom.students.all()
		print(students)
		serialized_students = UserSerializer(students, many=True)
		print("serialized_students")
		print(serialized_students.data)
		return Response(serialized_students.data)

	def post(self, request, format=None):
		classroom_id = request.data.get('id')
		classroom = Classroom.objects.get(id=classroom_id)
		student_ids = request.data.get('students')
		student_users = [User.objects.get(username=student_id) for student_id in student_ids]
		classroom.students.add(*student_users)
		classroom.save()
		serialized_classroom = ClassroomSerializer(classroom, many=False).data
		serialized_students = UserSerializer(classroom.students.all(), many=True).data
		serialized_classroom['students'] = serialized_students
		return Response(serialized_classroom)

	def put(self, request, format=None):
		classroom_id = request.data.get('classroom_id')
		classroom = Classroom.objects.get(id=classroom_id)
		student_ids = request.data.get('students_to_remove')
		creator = request.data.get('creator')
		classroom_creator = User.objects.get(username=creator)
		student_users = [User.objects.get(username=student_id) for student_id in student_ids]
		print(student_users)
		if(classroom.creator==classroom_creator):
			classroom.students.remove(*student_users)
			classroom.save()
			serialized_classroom = ClassroomSerializer(classroom, many=False).data	
			serialized_students = UserSerializer(classroom.students.all(), many=True).data
			serialized_classroom['students'] = serialized_students
			return Response(serialized_classroom)
		return Response({
				"errors": [
					"You can't remove students"
				]
			}, status=status.HTTP_400_BAD_REQUEST)

class ClassroomModeratorView(APIView):
	
	def get(self, request, format=None):
		classroom_id = request.GET.get('id')
		classroom = Classroom.objects.get(id=classroom_id)
		moderators = classroom.moderators.all()
		print(moderators)
		serialized_moderators = UserSerializer(moderators, many=True)
		print("serialized_moderators")
		print(serialized_moderators.data)
		return Response(serialized_moderators.data)

	def post(self, request, format=None):
		classroom_id = request.data.get('id')
		classroom = Classroom.objects.get(id=classroom_id)
		moderator_ids = request.data.get('moderators')
		moderator_users = [User.objects.get(username=moderator_id) for moderator_id in moderator_ids]
		print("student_users",*moderator_users)
		classroom.moderators.add(*moderator_users)
		print("classroom",classroom)
		classroom.save()
		print("classroom_after_save",classroom)
		serialized_classroom = ClassroomSerializer(classroom, many=False).data
		print("serialized_classroom",serialized_classroom)
		serialized_moderators = UserSerializer(classroom.moderators.all(), many=True).data
		print("serialized_moderators",serialized_moderators)
		serialized_classroom['moderators'] = serialized_moderators
		print(serialized_classroom )
		return Response(serialized_classroom)

	def put(self, request, format=None):
		classroom_id = request.data.get('classroom_id')
		classroom = Classroom.objects.get(id=classroom_id)
		moderator_ids = request.data.get('moderators_to_remove')
		creator = request.data.get('creator')
		classroom_creator = User.objects.get(username=creator)
		moderator_users = [User.objects.get(username=moderator_id) for moderator_id in moderator_ids]
		print(moderator_users)
		if(classroom.creator==classroom_creator):
			classroom.moderators.remove(*moderator_users)
			classroom.save()
			serialized_classroom = ClassroomSerializer(classroom, many=False).data	
			serialized_students = UserSerializer(classroom.moderators.all(), many=True).data
			serialized_classroom['moderators'] = serialized_students
			return Response(serialized_classroom)
		return Response({
				"errors": [
					"You can't remove moderators"
				]
			}, status=status.HTTP_400_BAD_REQUEST)




