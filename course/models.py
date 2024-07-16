from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=20)
    course_code=models.PositiveSmallIntegerField()
    topics=models.TextField()
    teacher_in_charge=models.CharField(max_length=20)
    duration=models.PositiveSmallIntegerField()
    students_enrolled=models.PositiveSmallIntegerField()
    department=models.CharField(max_length=20)
    start_date=models.DateField()
    end_date=models.DateField()
    assessment_method=models.CharField(max_length=30)

    
    def __str__(self):
       return f"{self.title} {self.course_code}"

