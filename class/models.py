from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_name= models.CharField(max_length=15)
    class_capacity=models.PositiveSmallIntegerField()
    class_teacher=models.CharField(max_length=20)
    number_of_students=models.PositiveSmallIntegerField()
    available_books=models.SmallIntegerField()
    color=models.CharField(max_length=20)
    whiteboard_number=models.PositiveSmallIntegerField()
    number_of_windows=models.PositiveSmallIntegerField()
    arts_number=models.PositiveSmallIntegerField()
    students_nationality=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} {self.class_capacity}"
   





