from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Assignment.models import Assignment, Submission
from Assignment.serializers import AssignmentSerializer, SubmissionSerializer
from Classroom.models import Classroom
from AuthUser.models import User
from Comment.serializers import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class AssignmentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		classroom_id = request.GET.get('classroom_id')
		try:
			classroom = Classroom.objects.get(id=classroom_id)
			if request.user.username == classroom.creator.username or request.user in classroom.moderators.all() or request.user in classroom.students.all():
				assignments = Assignment.objects.filter(classroom__id=classroom_id)
				serialized_assignments = AssignmentSerializer(assignments, many=True).data	
				return Response(serialized_assignments)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Classroom query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		try:
			classroom = Classroom.objects.get(id=request.data.get('classroom_id'))
			if classroom.creator.username == request.user.username:
				serializer = AssignmentSerializer(data=request.data)
				uploader = request.user
				if serializer.is_valid():
					serializer.save(uploader=uploader, classroom=classroom)
					return Response(serializer.data)
				else:
					return Response(serializer.errors)
			else:
				return Response({
					"error": "Only classroom owner can upload assignment."
					}, status=status.HTTP_400_BAD_REQUEST)
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
			if request.user.username == assignment.classroom.creator.username or request.user in assignment.classroom.moderators.all() or request.user in assignment.classroom.students.all():
				try:
					submission = Submission.objects.get(submitter__username=request.user.username, assignment__id=assignment.id)
					submission.attachment = request.data.get('attachment')
					submission.save()
					serializer = SubmissionSerializer(submission, many=False)
					return Response(serializer.data)
				except:
					serializer = SubmissionSerializer(data=request.data)
					if serializer.is_valid():
						serializer.save(submitter=request.user, assignment=assignment)
						return Response(serializer.data)
					else:
						return Response(serializer.errors)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Assignment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)


class AssignmentCommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		assignment_id = request.GET.get('assignment_id')
		try:
			assignment = Assignment.objects.get(id=assignment_id)
			if request.user.username == assignment.classroom.creator.username or request.user in assignment.classroom.moderators.all() or request.user in assignment.classroom.students.all():
				allComments = assignment.comments.all()
				serialized_comments = CommentSerializer(allComments, many=True)
				serialized_assignment = AssignmentSerializer(assignment, many=False)
				serialized_assignment.data['comments'] = serialized_comments
				return Response(serialized_assignment.data)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Assignment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		assignment_id = request.data.get('assignment_id')
		try:
			assignment = Assignment.objects.get(id=assignment_id)
			if request.user.username == assignment.classroom.creator.username or request.user in assignment.classroom.moderators.all() or request.user in assignment.classroom.students.all():
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
					assignment.comments.add(comment)
					assignment.save()
				allComments = assignment.comments.all()
				serialized_comments = CommentSerializer(allComments, many=True)
				serialized_assignment = AssignmentSerializer(assignment, many=False)
				serialized_assignment.data['comments'] = serialized_comments
				return Response(serialized_assignment.data)
			else:
				return Response({
					"error": "You aren't enrolled in this classroom."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({
				"error": "Assignment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)