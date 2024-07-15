from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import CourseSerializer
from rest_framework.response import Response

class CourseListView(APIView):
    def get(self,request):
        course=course.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)



