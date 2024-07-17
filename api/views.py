from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from rest_framework.response import Response

from .serializer import StudentSerializer
from .serializer import ClassroomSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import ClassPeriodSerializer



class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    

class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)
    

class ClassroomListView(APIView):
    def get(self,request):
        classroom=Classroom.objects.all()
        serializer=ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriod=classPeriod.objects.all()
        serializer=ClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)
