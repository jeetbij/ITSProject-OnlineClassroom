from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

from AuthUser.models import User
from Polls.models import Poll, PollOption
from PollResponse.models import PollResponse
from Classroom.models import Classroom
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AuthUser.serializers import UserSerializer
from PollResponse.serializers import PollResponseSerializer

class PollResponseView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		'''To get responses 
		Take poll_id
		return list of responses of that poll'''

		try:
			poll_id = request.GET.get('poll_id')
			poll_responses = PollResponse.objects.filter(poll__id=poll_id)
			poll_responses_serialized = PollResponseSerializer(poll_responses, many=True).data
			return Response(poll_responses_serialized)
		except Exception as e:
			return Response({
				"error": "Poll Response query for this poll doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		'''To add a response
		Take poll_id, poll_option_id
		return list of responses of that poll'''

		try:
			poll_response=PollResponse.objects.filter(poll=request.data.get('poll_id')).get(user=request.user)
			poll_response_serialized = PollResponseSerializer(poll_response,many=False).data
			return Response({
				"Alert":"Response Already Submitted",
				"reponse":poll_response_serialized
				})
		except:
			try:
				poll_response = PollResponse()
				poll_response.user = request.user
				poll_response.poll = Poll.objects.get(id=request.data.get('poll_id'))
				poll_response.poll_option = PollOption.objects.get(id=request.data.get('poll_option_id'))
				poll_response.save()
				print(poll_response)
				poll_response_serialized = PollResponseSerializer(poll_response,many=False).data
				return Response(poll_response_serialized)
			except Exception as e:
				return Response({
					"error": "Poll Response query for this poll or poll_option doesn't exists."
					}, status=status.HTTP_400_BAD_REQUEST)













