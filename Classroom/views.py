from rest_framework.views import APIView


from .models import Classroom
from .serializers import ClassroomSerializer
from AuthUser.serializers import UserSerializer
from AuthUser.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import status	

class ClassroomView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
<<<<<<< HEAD
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

=======
		classroom_id = request.GET.get('classroom_id')
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username:
				serializer = ClassroomSerializer(classroom, many=False)
				return Response(serializer.data)
			else:
				return Response({
					"error": "You are not authorized to access this classroom."
					}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({
				"error": "Classroom query does not exists."
				}, status=status.HTTP_403_FORBIDDEN)

	def post(self, request, format=None):
		try:
			classroom_name = request.data.get('name')
			classroom = Classroom()
			classroom.name = classroom_name
			classroom.creator = request.user
			classroom.save()
			serialized_classroom = ClassroomSerializer(classroom, many=False)
			return Response(serialized_classroom.data)
		except Exception as e:
			return Response({
				"error": "Something went wrong."
				}, status=status.HTTP_403_FORBIDDEN)
		
>>>>>>> 50880e0fa176306156d3fcb7d63cf70a9fcdd20b

class ClassroomStudentView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		classroom_id = request.GET.get('id')
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username:
				students = classroom.students.all()
				serialized_students = UserSerializer(students, many=True)
				return Response(serialized_students.data)
			else:
				return Response({
					"error": "You are not authorized to access this data."
					}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({
				"error": "Query does not exists."
				}, status=status.HTTP_403_FORBIDDEN)

	def post(self, request, format=None):
		classroom_id = request.data.get('id')
<<<<<<< HEAD
		classroom = Classroom.objects.get(id=classroom_id)
		student_ids = request.data.get('students')
		student_users = [User.objects.get(username=student_id) for student_id in student_ids]
		classroom.students.add(*student_users)
		classroom.save()
		serialized_classroom = ClassroomSerializer(classroom, many=False).data
		serialized_students = UserSerializer(classroom.students.all(), many=True).data
		serialized_classroom['students'] = serialized_students
		return Response(serialized_classroom)
=======
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username:
				student_ids = request.data.get('students')
				student_users = [User.objects.get(username=student_id) for student_id in student_ids]
				classroom.students.add(*student_users)
				classroom.save()
				serialized_classroom = ClassroomSerializer(classroom, many=False).data
				serialized_students = UserSerializer(classroom.students.all(), many=True).data
				serialized_classroom['students'] = serialized_students
				return Response(serialized_classroom)
			else:
				return Response({
					"error": "You are not authorized to add students to this classroom."
					}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({
				"error": "Query does not exists."
				}, status=status.HTTP_403_FORBIDDEN)
>>>>>>> 50880e0fa176306156d3fcb7d63cf70a9fcdd20b

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
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		classroom_id = request.GET.get('id')
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username:
				moderators = classroom.moderators.all()
				serialized_moderators = UserSerializer(moderators, many=True)
				return Response(serialized_moderators.data)
			else:
				return Response({
					"error": "You are not authorized to access this data."
					}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({
				"error": "Classroom query does not exists."
				}, status=status.HTTP_403_FORBIDDEN)

	def post(self, request, format=None):
		classroom_id = request.data.get('id')
<<<<<<< HEAD
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
=======
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username:
				moderator_ids = request.data.get('moderators')
				moderator_users = [User.objects.get(username=moderator_id) for moderator_id in moderator_ids]
				classroom.moderators.add(*moderator_users)
				classroom.save()
				serialized_classroom = ClassroomSerializer(classroom, many=False).data
				serialized_moderators = UserSerializer(classroom.moderators.all(), many=True).data
				serialized_classroom['moderators'] = serialized_moderators
				return Response(serialized_classroom)
			else:
				return Response({
					"error": "You are not authorized to add moderators to this classroom."
					}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_403_FORBIDDEN)



>>>>>>> 50880e0fa176306156d3fcb7d63cf70a9fcdd20b




