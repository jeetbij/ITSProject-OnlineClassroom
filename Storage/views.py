from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Storage.serializers import StorageSerializer, UploadDocumentSerializer
from Storage.models import Storage, UploadDocument

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class StorageView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, format=None):
		try:
			allDocuments = Storage.objects.get(user=request.user).allDocuments.all()
			serialized_storage = StorageSerializer(storage, many=False).data
			serialized_documents = UploadDocumentSerializer(allDocuments, many=True).data
			serialized_storage['documents'] = serialized_documents
			return Response(serialized_storage)
		except Exception as e:
			storage = Storage()
			storage.user = request.user
			storage.save()
			allDocuments = storage.allDocuments.all()
			serialized_storage = StorageSerializer(storage, many=False).data
			serialized_documents = UploadDocumentSerializer(allDocuments, many=True).data
			serialized_storage['documents'] = serialized_documents
			return Response(serialized_storage)


class UploadDocumentView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request, format=None):
		try:
			try:
				storage = Storage.objects.get(user=request.user)
			except Exception as e:
				print(e)
				storage = Storage()
				storage.user = request.user
				storage.save()
			document = request.FILES.get('document')
			uploadDocument = UploadDocument()
			uploadDocument.document = document
			uploadDocument.uploader = request.user
			uploadDocument.save()
			print(storage)
			storage.allDocuments.add(uploadDocument)
			serialized_document = UploadDocumentSerializer(uploadDocument, many=False)
			return  Response(serialized_document.data)
		except Exception as e:
			print(e)
			return Response({
				"error": "Storage is not allocated to your account."
				}, status=status.HTTP_400_BAD_REQUEST)