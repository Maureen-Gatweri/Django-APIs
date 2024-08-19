import email
from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from rest_framework.response import Response
from rest_framework import status

from .serializer import StudentSerializer, minimalClassRoomSerializer, minimalCourseSerializer, minimalTeacherSerializer
from .serializer import ClassroomSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from .serializer import ClassPeriodSerializer
from .serializer import Student
from .serializer import Teacher
from .serializer import Course
from .serializer import ClassPeriod
from .serializer import Classroom
from .serializer import minimalStudentSerializer
# from .models import Student
from rest_framework.response import Response



class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=minimalStudentSerializer(students, many=True)
        first_name=request.query_params.get("first_name")
        if first_name:
           students=students.filter(first_name=first_name)
      #   email=request.query_params.get("email")
        if email:
           students=students.filter(email=email) 

        return Response(serializer.data)
        
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def put (self,request,id):
       Student_instance=Student.objects.get(id=id)
       serializer=StudentSerializer(Student,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
          return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
   
    def delete(self,request,id):
       student=Student.objects.get(id=id)
       student.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  

class StudentDetailView(APIView):
   def get(self,request,id):
      Student=Student.objects.get(id=id)
      serializer=StudentSerializer(Student)
      return Response(serializer.data)  
   def enroll_student(self,student,course_code):
      course=Course.objects.get(id=course_code)
      student.course.add(course) 

   def post(self,request,id):
      Student=Student.objects.get(id=id)
      action=request.data.get("action")
      if action == "enroll":
         course_code=request.data.get("course")
         self.enroll_student(Student,course_code)
         return Response(status.HTTP_201_CREATED)


class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
      #   serializer=TeacherSerializer(teacher, many=True)
        serializer=minimalTeacherSerializer(teacher, many=True)
        first_name=request.query_params.get("first_name")
        email = request.query_params.get("email")
        if first_name:
           teachers=teachers.filter(first_name==first_name)
      #   email=request.query_params.get("email")
        if email:
           teachers=teachers.filter(email ==email) 
        return Response(serializer.data)
    
    def add_teacher(self,teacher,teacher_id):
      teacher=teacher.objects.get(id= teacher_id)
      teacher.course.add(teacher) 
    
    def post(self,request,id):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
       teacher=Teacher.objects.get(id=id)
       teacher.delete()
       return Response(status=status.HTTP_202_ACCEPTED)      

class TeacherDetailView(APIView):
   def get(self,request,id):
      teacher=Teacher.objects.get(id=id)
      serializer=TeacherSerializer(Teacher)
      return Response(serializer.data)       
    
    
class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all()
      #   serializer=CourseSerializer(course, many=True)
        
        serializer=minimalCourseSerializer(course, many=True)
        department=request.query_params.get("course_code")
        topics = request.query_params.get("topics")
        if department:
           courses=courses.filter(department == department)
      #   email=request.query_params.get("email")
        if topics:
           courses=courses.filter(topics ==topics) 
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
                 
    def put (self,request,id):
       course=Course.objects.get(id=id)
       serializer=CourseSerializer(Course,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
          return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
        

    def delete(self,request,id):
       course=Course.objects.get(id=id)
       course.delete()
       return Response(status=status.HTTP_202_ACCEPTED)   

class CourseDetailView(APIView):
   def get(self,request,id):
      course=Course.objects.get(id=id)
      serializer=CourseSerializer(Course)
      return Response(serializer.data)         
    
    

class ClassroomListView(APIView):
    def get(self,request):
        classroom=Classroom.objects.all()
      #   serializer=ClassroomSerializer(classroom, many=True)
        serializer=minimalClassRoomSerializer(classroom, many=True)
        color=request.query_params.get("color")
        classes = request.query_params.get("class_capacity")
        if classes:
           courses=courses.filter(classes == classes)
      #   email=request.query_params.get("email")
        if color:
           courses=courses.filter(color == color) 
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ClassroomSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
            
    def put (self,request,id):
       classroom=Classroom.objects.get(id=id)
       serializer=ClassroomSerializer(Classroom,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
          return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
        
    def delete(self,request,id):
       classRoom=Classroom.objects.get(id=id)
       classRoom.delete()
       return Response(status=status.HTTP_202_ACCEPTED) 
    
class ClassroomDetailView(APIView):
   def get(self,request,id):
      Classroom=Classroom.objects.get(id=id)
      serializer=ClassroomSerializer(Classroom)
      return Response(serializer.data) 
            
    
    
class ClassPeriodListView(APIView):
    def get(self,request):
        classPeriod=classPeriod.objects.all()
        serializer=ClassPeriodSerializer(classPeriod, many=True)
      #   serializer=minimalClassRoomSerializer(ClassPeriod, many=True)
      #   color=request.query_params.get("color")
      #   classes = request.query_params.get("class_capacity")
      #   if :
      #      courses=courses.filter(start_time == start_time)
      # #   email=request.query_params.get("email")
      #   if newPeriod:
      #      courses=courses.filter(color == color) 
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put (self,request,id):
       classPeriod=classPeriod.objects.get(id=id)
       serializer=ClassPeriodSerializer(classPeriod,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
          return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
   
    def delete(self,request,id):
       classPeriod=classPeriod.objects.get(id=id)
       classPeriod.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  

class ClassPeriodDetailView(APIView):
   def get(self,request,id):
      classPeriod=ClassPeriod.objects.get(id=id)
      serializer=ClassPeriodSerializer(classPeriod)
      return Response(serializer.data)     
    

         
    

