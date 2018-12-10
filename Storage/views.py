from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Storage.serializers import StorageSerializer, UploadDocumentSerializer
from Storage.models import Storage, UploadDocument

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

def checkSize(request):
	storage = Storage.objects.filter(user=request.user)[0]
	allDocuments = storage.allDocuments.all()
	size = 0
	for doc in allDocuments:
		try:
			size+=doc.document.file.size
		except:
			pass
	return size

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
			try:
				storage = Storage.objects.filter(user=request.user)[0]
			except Exception as e:
				print(e)
				storage = Storage()
				storage.user = request.user
				storage.save()
			allDocuments = storage.allDocuments.all().order_by('uploaded_on')[::-1]
			usedSize = checkSize(request)
			serialized_storage = StorageSerializer(storage, many=False).data
			serialized_documents = UploadDocumentSerializer(allDocuments, many=True).data
			serialized_storage['documents'] = serialized_documents
			serialized_storage['size'] = usedSize
			return Response(serialized_storage)


class UploadDocumentView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request, format=None):
		try:
			try:
				storage = Storage.objects.filter(user=request.user)[0]
			except Exception as e:
				print(e)
				storage = Storage()
				storage.user = request.user
				storage.save()
			document = request.FILES.get('document')
			if checkSize(request)+document.size <= storage.limit:
				uploadDocument = UploadDocument()
				uploadDocument.document = document
				uploadDocument.uploader = request.user
				uploadDocument.save()
				storage.allDocuments.add(uploadDocument)
				serialized_document = UploadDocumentSerializer(uploadDocument, many=False)
				return  Response(serialized_document.data)
			else:
				return Response({
				"error": "You don't have enough space."
				}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({
				"error": "Storage is not allocated to your account."
				}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		try:
			document = UploadDocument.objects.get(id=request.GET.get('id'))
			if document.uploader == request.user:
				document.delete()
				return Response({
					"success": "Document deleted successfully."
					}, status=status.HTTP_200_OK)
			else:
				return Response({
					"error": "You are not authorized to delete this document."
					}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({
				"error": "Document does not exists."
				}, status=status.HTTP_400_BAD_REQUEST)			