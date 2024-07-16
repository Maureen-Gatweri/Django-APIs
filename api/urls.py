from django.urls import path
from api.views import StudentListView
from api.views import ClassroomListView
from api.views import TeacherListView
from api.views import  CourseListView

urlpatterns= [
    path( "students/", StudentListView.as_view(), name = 
         "student_list_view"),
    path( "classroom/", ClassroomListView.as_view(), name = 
         "classroom_list_view"),
    path( "course/", CourseListView.as_view(), name = 
         "course_list_view"),
    path( "teacher/", TeacherListView.as_view(), name = 
         "teacher_list_view")
]