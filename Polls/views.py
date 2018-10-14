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
	
# 	type 1: Add Poll
# 	{
# 	"type":1,
# 	"classroom_id":1,
# 	"poll_text":"Which Bike",
# 	}

# 	type 2: Add PollOptions
# 	{
# 		"type":2,
# 		"parent_poll_id": 5,
# 		"poll_option_text":"KTM 2"
# 	}


	def post(self, request, format=None):
		try:
			query_type = request.data.get('type')
			if(query_type==1):
				classroom_id = request.data.get('classroom_id')
				classroom = Classroom.objects.get(id=classroom_id)
				poll = Poll()
				poll.creater = request.user
				poll.classroom = classroom
				poll.poll_text = request.data.get('poll_text')
				poll.save()
				print(poll)
				poll_serialized = PollSerializer(poll,many=False).data
				return Response(poll_serialized)
			elif(query_type==2):
				parrent_poll_id = request.data.get('parent_poll_id')
				poll_option = PollOption()
				poll_option.parrent_poll = Poll.objects.get(id=parrent_poll_id)
				poll_option.option_text = request.data.get('poll_option_text')
				poll_option.save()
				print(poll_option)
				poll_option_serialized = PollOptionSerializer(poll_option,many=False).data
				return Response(poll_option_serialized)
			return Response({
				"error": "Type value is not defined."
			}, status=status.HTTP_400_BAD_REQUEST)

		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
			}, status=status.HTTP_400_BAD_REQUEST)









		
