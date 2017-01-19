from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import random, string
from smart_selects.db_fields import ChainedManyToManyField

# Create your models here.

#This is the model for a student
@python_2_unicode_compatible
class Student(models.Model):
    Student_First_Name = models.CharField(max_length=200)
    Student_Last_Name = models.CharField(max_length=200)
    Student_ID_Number = models.CharField(max_length=200, unique=True)
    Student_Class = models.ManyToManyField('Class', blank=True)
    Professor = models.ForeignKey(User,null=True)
    def __str__(self):
        return self.Student_Last_Name + ',' + self.Student_First_Name

# This is the model for a class
@python_2_unicode_compatible
class Class(models.Model):  
    class Meta:
        verbose_name_plural = "Classes"
    Class_Name = models.CharField(max_length=200)
    Student_List = models.ManyToManyField('Student', related_name='class_list')
    Professor = models.ForeignKey(User,null=True)
    AddCode = models.IntegerField
    pass
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

#This is the model for attendance records
class AttendanceRecord(models.Model):
    class Meta:
        verbose_name = "Attendance Record"
        unique_together = ["Associated_Class", "Date"]
    Associated_Class = models.ForeignKey(Class)
    Date = models.DateField()
    Present_Students = ChainedManyToManyField(Student, chained_field="Associated_Class", chained_model_field="Student_Class",)
    def get_associated_class_id(self):
        return self.Associated_Class
    def __str__(self):
        return self.Associated_Class.__str__() + ' on date ' + self.Date.__str__()
   
    
