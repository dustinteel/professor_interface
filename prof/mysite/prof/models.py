from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import random, string

# Create your models here.

#This is the model for a student
@python_2_unicode_compatible
class Student(models.Model):
    pass
    Student_First_Name = models.CharField(max_length=200)
    Student_Last_Name = models.CharField(max_length=200)
    Student_ID_Number = models.CharField(max_length=200)
    Student_Class = models.ForeignKey('Class', null=True)
    def __str__(self):
        return self.Student_Last_Name + ',' + self.Student_First_Name

# This is the model for a class
@python_2_unicode_compatible
class Class(models.Model):  
    Class_Name = models.CharField(max_length=200)
    Student_List = models.ManyToManyField('Student', related_name='class_list')
    Professor = models.ForeignKey(User,null=True)
    AddCode = models.IntegerField
    def __str__(self):
        return self.Class_Name
    def getName(self):
        return self.Class_Name
    def getProfessor(self):
        return self.Professor.id
    def getProf(self):
        return self.Professor
    def getStudents(self):
        return self.Student_List
    pass


def get_limit_choices_to():
        return Student.objects.filter(class_list__in = instance)

#This is the model for attendance records
class AttendanceRecord(models.Model):
    Associated_Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    Date = models.DateField()
    Absent_Students = models.ManyToManyField('Student')
    Present_Students = models.ManyToManyField('Student', related_name='a')
    def get_associated_class_name(self):
        return self.Associated_Class.__str__()
    def __str__(self):
        return self.Associated_Class.__str__() + ' on date ' + self.Date.__str__(self)
   
    
