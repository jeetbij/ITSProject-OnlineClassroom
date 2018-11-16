from django.contrib import admin
from Storage.models import UploadDocument, Storage
# Register your models here.

admin.site.register(UploadDocument),
admin.site.register(Storage)