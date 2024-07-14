from django.db import models

# Create your models here.
class Teacher (models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    bio=models.TextField(max_length=50)
    phone_number=models.CharField(max_length=15)
    specialization=models.CharField(max_length=25)
    qualifications=models.CharField(max_length=30)
    teacher_id=models.PositiveSmallIntegerField()
    country=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




