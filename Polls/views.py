from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

from AuthUser.models import User
from Polls.models import Poll, PollOption, PollResponse
from Classroom.models import Classroom

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AuthUser.serializers import UserSerializer
from Polls.serializers import PollSerializer,PollOptionSerializer,PollResponseSerializer
# Create your views here.
class PollView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			classroom_id = request.GET.get('classroom_id')
			classroom = Classroom.objects.get(id=classroom_id)
			polls = Poll.objects.filter(classroom=classroom) 
			print(polls)
			poll_list=[]
			for poll in polls:
				poll_serialized = PollSerializer(poll,many=False).data
				poll_options = PollOption.objects.filter(parrent_poll=poll)
				poll_options_serialized = PollOptionSerializer(poll_options,many=True).data
				poll_serialized['poll_options'] = poll_options_serialized
				poll_list.append(poll_serialized)
			return Response(poll_list)
		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)
	
		
