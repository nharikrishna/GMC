from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    roll_number = models.CharField(max_length=5)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


class Advisor(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


class Faculty(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Faculties'


class Course(models.Model):
    course_title = models.CharField(primary_key=True, max_length=10)
    year = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


class FacultyCourse(models.Model):
    username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE)

