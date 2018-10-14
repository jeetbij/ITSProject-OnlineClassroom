from django.contrib import admin
from Polls.models import Poll, PollOption
# Register your models here.

admin.site.register(Poll)
admin.site.register(PollOption)