from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Assignment.models import Assignment
from Assignment.serializers import AssignmentSerializer
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