# Generated by Django 5.0.6 on 2024-08-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0002_remove_student_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]