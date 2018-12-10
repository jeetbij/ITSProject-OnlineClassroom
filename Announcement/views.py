from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Announcement.models import Announcement
from Announcement.serializers import AnnouncementSerializer
from AuthUser.serializers import UserSerializer
from AuthUser.models import User
from Classroom.models import Classroom
from Comment.serializers import CommentSerializer
from Classroom.serializers import ClassroomSerializer
from Comment.models import Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Notifications.views import Notify
from Notifications.models import Notification

class AnnouncementView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		'''To get announcements from a classroom.
		Takes classroom_id.
		returns list of announcements in that classroom.'''

		classroom_id = request.GET.get('classroom_id')
		try:
			announcements = Announcement.objects.filter(classroom__id=classroom_id)
			serializer = AnnouncementSerializer(announcements, many=True)
			return Response(serializer.data)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		'''To post announcements in a classroom.
		Takes content, announcer, classroom_id.
		returns the announcement object.'''

		try:
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			if request.user.username == classroom.creator.username:
				serializer = AnnouncementSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save(announcer=request.user, classroom=classroom)
					students = classroom.students.all()
					msg = "A new announcement is posted in "+ str(classroom.name) +"."
					Notify(sender=request.user, receiver=[student for student in students], type=Notification.C, text=msg)
					return Response(serializer.data)
				else:
					return Response(serializer.errors)
			else:
				return Response({
					"error": "You aren't authorized to add data in this classroom."
					}, status = status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, format=None):
		'''To edit announcements in a classroom.
		Takes content, classroom_id.
		returns the announcement object.'''

		try:
			announcement_id = request.data.get('annoucement_id')
			announcement = Announcement.objects.get(id=announcement_id)
			if request.user.username == announcement.announcer.username:
				announcement.content = request.data.get('content')
				announcement.save()
				students = announcement.classroom.students.all()
				msg = "A announcement is updated in "+ str(classroom.name) +"."
				Notify(sender=request.user, receiver=[student for student in students], type=Notification.C, text=msg)
				announcement_serializer = AnnouncementSerializer(announcement, many=False).data
				return Response(announcement_serializer)
			return Response({
					"errors": [
						"You can't update this announcement"
					]
				}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "You are not authorized to make changes in this classroom."
				}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		'''To delete announcements in a classroom.
		Takes annoucement_id.
		returns the deleted announcement object with a message.'''

		announcement_id = request.data.get('annoucement_id')
		announcement = Announcement.objects.get(id=announcement_id)
		if request.user.username == announcement.announcer.username:
			announcement_serializer = AnnouncementSerializer(announcement, many=False).data
			announcement.delete()
			return Response({
				"Action":"This announcement is deleted.",
				"Announcement":announcement_serializer
				})


class AnnoucementCommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		'''To get comment in an announcement.
		Takes annoucement_id.
		returns the announcement object with a list of comments.'''

		try:
			announcement = Announcement.objects.get(id=request.GET.get('id'))
			if request.user.username == announcement.classroom.creator.username or request.user in announcement.classroom.moderators.all() or request.user in announcement.classroom.students.all():
				announcement_serializer = AnnouncementSerializer(announcement, many=False).data
				allcomments = announcement.comment.all()
				print("Start")
				comments_serialized=[]
				for comment in allcomments:
					serializedcomment = CommentSerializer(comment, many=False).data
					if(request.user in comment.upvoters.all()):
						serializedcomment['has_Upvoted']=1
					else:
						serializedcomment['has_Upvoted']=0
					if(request.user in comment.downvoters.all()):
						serializedcomment['has_Downvoted']=1
					else:
						serializedcomment['has_Downvoted']=0
					comments_serialized.append(serializedcomment)
				announcement_serializer['comments'] = comments_serialized
				serializedclassroom = ClassroomSerializer(announcement.classroom, many=False)
				announcement_serializer['classroom'] = serializedclassroom.data
				return Response(announcement_serializer)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Announcement query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		'''To post a comment in an announcement.
		Takes annoucement_id, parrent_comment_id and comment_text.
		returns the announcement object with a list of comments.'''

		announcement_id = request.data.get('announcement_id')
		try:
			announcement = Announcement.objects.get(id=announcement_id)
			if request.user.username == announcement.classroom.creator.username or request.user in announcement.classroom.moderators.all() or request.user in announcement.classroom.students.all():
				comment = Comment()
				if request.data.get('comment_id'):
					try:
						comment.parent = Comment.objects.get(id=request.data.get('comment_id'))
						comment.commenter = request.user
						comment.comment_text = request.data.get('content')
						comment.save()
					except Exception as e:
						return Response({
							"error": "Comment query doesn't exists."
							}, status=status.HTTP_400_BAD_REQUEST)
				else:
					comment.parent = None
					comment.commenter = request.user
					comment.comment_text = request.data.get('content')
					comment.save()
					announcement.comment.add(comment)
					announcement.save()
				allComments = announcement.comment.all()
				serialized_comments = CommentSerializer(allComments, many=True).data
				serialized_announcement = AnnouncementSerializer(announcement, many=False).data
				serialized_announcement['comments'] = serialized_comments
				return Response(serialized_announcement)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Announcement query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)





