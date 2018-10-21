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
from Polls.serializers import PollSerializer,PollOptionSerializer
# Create your views here.
class PollView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			classroom_id = request.GET.get('classroom_id')
			classroom = Classroom.objects.get(id=classroom_id)
			polls = Poll.objects.filter(classroom=classroom) 
			poll_list=[]
			for poll in polls:
				poll_serialized = PollSerializer(poll,many=False).data
				poll_options = PollOption.objects.filter(parrent_poll=poll)
				poll_options_serialized = PollOptionSerializer(poll_options,many=True).data
				poll_serialized['poll_options'] = poll_options_serialized
				poll_serialized['is_responded'] = '0'
				print(PollResponse.objects.filter(poll=poll))
				print(PollResponse.objects.filter(poll=poll).filter(user=request.user))
				if(PollResponse.objects.filter(poll=poll).filter(user=request.user)):
					poll_serialized['is_responded'] = '1'
				else:
					poll_serialized['is_responded'] = '0'
				poll_list.append(poll_serialized)
			return Response(poll_list)
		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)
	



	def post(self, request, format=None):
		'''	type 1: Add Poll
			{
			"type":1,
			"classroom_id":1,
			"poll_text":"Which Bike",
			}

			type 2: Add PollOptions
			{
				"type":2,
				"parent_poll_id": 5,
				"poll_option_text":"KTM 2"
			}'''

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
				poll_serialized = PollSerializer(poll,many=False).data
				return Response(poll_serialized)
			elif(query_type==2):
				parrent_poll_id = request.data.get('parent_poll_id')
				poll_option = PollOption()
				poll_option.parrent_poll = Poll.objects.get(id=parrent_poll_id)
				poll_option.option_text = request.data.get('poll_option_text')
				poll_option.save()
				poll_option_serialized = PollOptionSerializer(poll_option,many=False).data
				return Response(poll_option_serialized)
			return Response({
				"error": "Type value is not defined."
			}, status=status.HTTP_400_BAD_REQUEST)

		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
			}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		poll = Poll.objects.get(id=request.data.get('poll_id'))
		poll_serialized = PollSerializer(poll,many=False)
		print("poll",poll)
		poll.delete()
		print("poll",poll)
		return Response("Poll deleted")













		
