from django.urls import path
from api.views import StudentListView
from api.views import ClassroomListView
from api.views import TeacherListView
from api.views import  CourseListView
from api.views import ClassPeriodListView

from api.views import StudentDetailView
from api.views import ClassPeriodDetailView
from api.views import CourseDetailView
from api.views import TeacherDetailView
from api.views import ClassroomDetailView


urlpatterns= [
    path( "students/", StudentListView.as_view(), name = 
         "student_list_view"),
    path( "classroom/", ClassroomListView.as_view(), name = 
         "classroom_list_view"),
    path( "course/", CourseListView.as_view(), name = 
         "course_list_view"),
    path( "teacher/", TeacherListView.as_view(), name = 
         "teacher_list_view"),
     path( "ClassPeriod/", ClassPeriodListView.as_view(), name = 
         "ClassPeriod_list_view"),


     path( "students/<int:id>/", StudentDetailView.as_view(),name = 
         "Student_detail_view"),
     path( "Teachers/<int:id>/", TeacherDetailView.as_view(),name = 
         "Teacher_detail_view"),
     path( "courses/<int:id>/", CourseDetailView.as_view(),name = 
         "Course_detail_view"),
    path( "courses/<int:id>/", ClassroomDetailView.as_view(),name = 
         "Course_detail_view"),
     path( "courses/<int:id>/", ClassPeriodDetailView.as_view(),name = 
         "Course_detail_view")
]