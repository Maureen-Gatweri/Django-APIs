from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from classPeriod.models import ClassPeriod
from rest_framework import renderers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields="__all__"
class minimalCourseSerializer(serializers.ModelSerializer):
      course_details=serializers.SerializerMethodField()
      def get_course_details(self,object):
         return f" {object.course_code} {object.title}"
       
      class Meta:
          model=Course
          fields= ["topics", "department","course_details"]  


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= "__all__"


class minimalStudentSerializer(serializers.ModelSerializer):
      full_name=serializers.SerializerMethodField()
      def get_full_name(self,object):
         return f" {object.first_name} {object.last_name}"
       
      class Meta:
          model=Student
          fields= ["full_name", "email","full_name"]
    
      
      
      

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields="__all__"

class minimalTeacherSerializer(serializers.ModelSerializer):
      full_name=serializers.SerializerMethodField()
      def get_full_name(self,object):
         return f" {object.first_name} {object.last_name}"
       
      class Meta:
          model=Teacher
          fields= ["class_name", "email","class_capacity"] 




class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classroom
        fields="__all__"    

class minimalClassRoomSerializer(serializers.ModelSerializer):
      class_details=serializers.SerializerMethodField()
      def get_class_details(self,object):
         return f" {object.class_name} {object.class_teacher}"
       
      class Meta:
          model=Classroom
          fields= ["color","class_name","class_details"]


class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields="_all_"

# class minimalClassPerioderializer(serializers.ModelSerializer):
#       period=serializers.SerializerMethodField()
#       def get_period(self,object):
#          return f" {object.start_time} {object.end_time}"
       
#       class Meta:
#           model=ClassPeriod
#           fields= ["start_time","end_time","period"]





