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
from PollResponse.serializers import PollResponseSerializer
from Notifications.views import Notify, sendMail 
from Notifications.models import Notification
# Create your views here.
class PollView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		''' To get polls and its poll options from a class.
		Takes classroom_id
		Return poll list with its options'''
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
				poll_response=PollResponse.objects.filter(poll=poll,user=request.user)
				if(poll_response):	
					poll_response_serialized = PollResponseSerializer(poll_response[0],many=False).data
					poll_serialized['is_responded'] = poll_response_serialized
				else:
					poll_serialized['is_responded'] = 0
				poll_list.append(poll_serialized)
			return Response(poll_list)
		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)
	
	def post(self, request, format=None):
		'''	To add poll and poll options.
		Take:
			type 1: Add Poll
			{
				"type":1,
				"classroom_id":1,
				"poll_text":"Which Bike"
			}
			type 2: Add PollOptions
			{
				"type":2,
				"parent_poll_id": 5,
				"poll_option_text":"KTM 2"
			}

		Returns:
			poll object or polloption object'''

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

				students = classroom.students.all()
				msg = "A new poll is posted in "+ str(classroom.name) +"."
				Notify(sender=request.user, receiver=[student for student in students], type=Notification.P, text=msg)
				sendMail(recipient=[student.email for student in students],subject="Aphlabet Notification",body= msg )
				
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
			print(e)
			return Response({
				"error": "Classroom query for polls doesn't exists."
			}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		'''To delete a poll.
		Takes poll_id
		returns a msg'''
		poll = Poll.objects.get(id=request.data.get('poll_id'))
		poll_serialized = PollSerializer(poll,many=False)
		poll.delete()
		return Response("Poll deleted")


class PollDetail(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		''' To get polls and its poll options from a class.
		Takes classroom_id
		Return poll list with its options'''
		try:
			poll_id = request.GET.get('poll_id')
			poll_options = PollOption.objects.filter(parrent_poll__id=poll_id) 
			res = []
			op = []
			count = []
			for option in poll_options:
				op.append(str(option.option_text))
				count.append(0)
			print(op, count)
			poll_responses=PollResponse.objects.filter(poll__id=poll_id)
			for poll_response in poll_responses:
				for o in op:
					i=0
					if str(poll_response) == str(o):
						count[i]+=1
						break
					i+=1
			i=0
			for co in count:
				res.append({str(op[i]):count[i]})
				i+=1
			print(res)

			return Response(res
				, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({
				"error": "Classroom query for polls doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)
