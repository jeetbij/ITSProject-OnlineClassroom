from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Assignment.models import Assignment, Submission
from Assignment.serializers import AssignmentSerializer, SubmissionSerializer
from Classroom.models import Classroom
from AuthUser.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class AssignmentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		classroom_id = request.GET.get('classroom_id')
		assignments = Assignment.objects.filter(uploader__username=request.user.username, classroom__id=classroom_id)
		serialized_assignments = AssignmentSerializer(assignments, many=True).data

		return Response(serialized_assignments)

	def post(self, request, format=None):
		try:
			serializer = AssignmentSerializer(data=request.data)
			uploader = request.user
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			if serializer.is_valid():
				serializer.save(uploader=uploader, classroom=classroom)
				return Response(serializer.data)
			else:
				return Response(serializer.errors)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)


class SubmissionView(APIView):
	permission_classes = (IsAuthenticated, )
	
	def get(self, request, format=None):
		assignment_id = request.GET.get('assignment_id')
		try:
			assignment = Assignment.objects.get(id=assignment_id)
			if request.user.username == assignment.classroom.creator.username:
				submissions = Submission.objects.filter(assignment__id=assignment.id)
				serialized_submissions = SubmissionSerializer(submissions, many=True)
				return Response(serialized_submissions.data)
			else:
				submissions = Submission.objects.filter(assignment__id=assignment.id, submitter__username=request.user.username)
				serialized_submissions = SubmissionSerializer(submissions, many=True)
				return Response(serialized_submissions.data)
		except Exception as e:
			return Response({
				"error": "Assignment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		assignment_id = request.data.get('assignment_id')
		try:
			assignment = Assignment.objects.get(id=assignment_id)
			serializer = SubmissionSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save(submitter=request.user, assignment=assignment)
				return Response(serializer.data)
			else:
				return Response(serializer.errors)
		except Exception as e:
			return Response({
				"error": "Assignment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)