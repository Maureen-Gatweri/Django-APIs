from django.urls import path
from api.views import TeacherListView

urlpatterns= [
    path( "teacher/", TeacherListView.as_view(), name = 
         "teacher_list_view"),
]