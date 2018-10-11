from django.conf.urls import url
from Comment.views import CommentView

app_name = 'Comment'

urlpatterns = [
	url(r'^$', CommentView.as_view(), name='commentview')
	]