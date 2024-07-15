from django.urls import path
from api.views import ClassroomListView

urlpatterns= [
    path( "class/", ClassroomListView.as_view(), name = 
         "Classroom_list_view"),
]