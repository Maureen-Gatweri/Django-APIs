from django.urls import path
from api.views import CourseListView

urlpatterns= [
    path( "course/", CourseListView.as_view(), name = 
         "course_list_view"),
]