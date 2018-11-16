from django.conf.urls import url
from Storage.views import StorageView, UploadDocumentView

app_name = 'Storage'

urlpatterns = [
	url(r'^$', StorageView.as_view(), name='storageview'),
	url(r'^uploaddocument/$', UploadDocumentView.as_view(), name='uploaddocumentview'),
	]