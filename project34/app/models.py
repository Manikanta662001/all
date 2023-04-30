from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=100)
    principle=models.CharField(max_length=100)
class Student(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()