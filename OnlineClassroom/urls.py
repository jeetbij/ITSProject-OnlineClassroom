"""OnlineClassroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userauth/', include('AuthUser.urls')),
    path('classroom/', include('Classroom.urls')),
    path('comment/', include('Comment.urls')),
    path('announcement/', include('Announcement.urls')),
    path('assignment/', include('Assignment.urls')),
    path('polls/', include('Polls.urls')),
    path('resources/', include('Resources.urls')),
    path('storage/', include('Storage.urls')),
    path('poll_response/', include('PollResponse.urls')),
    path('notification/', include('Notifications.urls')),

    url(r'^docs/', include_docs_urls(title='Aphlabet Docs')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
