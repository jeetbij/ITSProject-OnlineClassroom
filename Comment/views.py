from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from Comment.models import Comment
from AuthUser.models import User
from Comment.serializers import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AuthUser.serializers import UserSerializer
# Create your views here.

class CommentView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			comment = Comment.objects.get(id=request.GET.get('id'))
			print(comment)
			child_comments = comment.child_comment.all()
			upvoters = comment.upvoters.all()
			downvoters = comment.downvoters.all()
			serialized_comments = CommentSerializer(child_comments, many=True).data
			serializer = CommentSerializer(comment, many=False).data
			serialized_upvotes = UserSerializer(upvoters,many=True).data
			serialized_downvoters = UserSerializer(downvoters,many=True).data

			serializer['child'] = serialized_comments
			serializer['upvoters'] = serialized_upvotes
			serializer['downvoters'] = serialized_downvoters
			print(serializer)
			return Response(serializer)
		except Exception as e:
			return Response({
				"error": "Comment query doesn't exists."
				}, status=status.HTTP_400_BAD_REQUEST)

# type 1: comment edit
# type 2: upvote
# type 3: downvote

	def put(self, request, format=None):
		try:
			comment = Comment.objects.get(id=request.data.get('comment_id'))
			query_type = request.data.get('type')
			if(query_type == 1):
				if(comment.commenter==request.user):
					comment.comment_text = request.data.get('comment_text')
					comment.save()
					serializer = CommentSerializer(comment,many=False)
					return Response(serializer.data)
				return Response({
					"error": "Can't edit this comment."
				}, status=status.HTTP_400_BAD_REQUEST)

			elif(query_type == 2):
				upvoter = request.user
				comment.upvoters.add(upvoter)
				print(comment)
				comment.save()
				serializer = CommentSerializer(comment,many=False)
				return Response(serializer.data)

			elif(query_type == 3):
				downvoter = request.user
				comment.downvoters.add(downvoter)
				print(comment)
				comment.save()
				serializer = CommentSerializer(comment,many=False)
				return Response(serializer.data)
			return Response({
				"error": "Type value is not defined."
			}, status=status.HTTP_400_BAD_REQUEST)
		
		except Exception as e:
			return Response({
				"error": "Comment query doesn't exists."
			}, status=status.HTTP_400_BAD_REQUEST)


# type 1: remove upvote
# type 2: remove downvote
	def delete(self, request, format=None):
		try:
			print(request.data)
			comment = Comment.objects.get(id=request.data.get('comment_id'))
			query_type = request.data.get('type')
			if(query_type == 1):
				remove_upvoter = request.user
				comment.upvoters.remove(remove_upvoter)
				comment.save()
				serializer = CommentSerializer(comment,many=False)
				return Response(serializer.data)

			elif(query_type == 2):
				remove_downvoter = request.user
				comment.downvoters.remove(remove_downvoter)
				comment.save()
				serializer = CommentSerializer(comment,many=False)
				return Response(serializer.data)
			return Response({
				"error": "Type value is not defined."
			}, status=status.HTTP_400_BAD_REQUEST)
		
		except Exception as e:
			print(e)
			return Response({
				"error": "Comment query doesn't exists."
			}, status=status.HTTP_400_BAD_REQUEST)











