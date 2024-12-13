"""
URL configuration for salvo_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from tracker.views import add_members,home,view_members,upload_attendance_file,view_meetings,add_minutes,member_stats,meeting_stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',home),
    path('add_member/',add_members),
    path('view_members/',view_members),
    path('upload_attendance_file/',upload_attendance_file),
    path('view_meetings/',view_meetings),
    path('add_minutes/<str:code>/',add_minutes),
    path('member_stats/',member_stats),
    path('meeting_stats/',meeting_stats),
]
