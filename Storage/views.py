from django.shortcuts import render
from rest_framwork.views import APIView
from rest_framework.response import Response
from Storage.serializers import StorageSerializer, UploadDocumentSerializer
from Storage.models import Storage
# Create your views here.

class StorageView(APIView):

	def get(request, *args, **kwargs):
		try:
			allDocuments = Storage.objects.get(user=request.user).allDocuments.all()
			serialized_documents = StorageSerializer(allDocuments, many=True).data
			return Response(serialized_documents)
		except Exception as e:
			storage = Storage()
			storage.user = request.user
			storage.save()
			allDocuments = storage.allDocuments.all()
			serialized_documents = StorageSerializer(allDocuments, many=True).data
			return Response(serialized_documents)


class UploadDocumentView(APIView):

	def post(request, *args, **kwargs):
		try:
			try:
				storage = Storage.objects.get(user=request.user)
			except Exception as e:
				storage = Storage()
				storage.user = request.user
				storage.save()
			document = request.FILES.get('document')
			uploadDocument = UploadDocument()
			uploadDocument.document = document
			uploadDocument.save()
			storage.allDocuments.add(uploadDocument)
			serialized_document = UploadDocumentSerializer(uploadDocument, many=False)
			return  Response(serialized_document.data)
		except Exception as e:
			return Response({
				"error": "Storage is not allocated to your account."
				}, status=status.HTTP_400_BAD_REQUEST)