from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Assignment.models import Assignment, Submission
from Assignment.serializers import AssignmentSerializer, SubmissionSerializer
from AuthUser.models import User
# Create your views here.

class AssignmentView(APIView):

	def get(self, request, format=None):
		assignments = Assignment.objects.filter(uploader__username=request.GET.get('username'))
		serialized_assignments = AssignmentSerializer(assignments, many=True).data

		return Response(serialized_assignments)

	def post(self, request, format=None):
		serializer = AssignmentSerializer(data=request.data)
		if serializer.is_valid():
			uploader = User.objects.get(username=request.data.get('username'))
			serializer.save(uploader=uploader)
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class SubmissionView(APIView):

	def get(self, request, format=None):
		assignment_id = request.GET.get('assignment_id')
		submissions = Submission.objects.filter(assignment__id=assignment_id)
		serialized_submissions = SubmissionSerializer(submissions, many=True)

		return Response(serialized_submissions.data)

	def post(self, request, format=None):
		assignment_id = request.data.get('assignment_id')
		assignment = Assignment.objects.get(id=assignment_id)
		submitter = User.objects.get(username=request.data.get('username'))
		serializer = SubmissionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(submitter=submitter, assignment=assignment)
			return Response(serializer.data)
		else:
			return Response(serializer.errors)