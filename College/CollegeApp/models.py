from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	uname=models.CharField(max_length=40)

	




class Faculty(models.Model):
	fname=models.CharField(max_length=40)
	feducation=models.CharField(max_length=40)
	fdep=models.CharField(max_length=40)
	femail=models.EmailField(max_length=30)
	faddress=models.CharField(max_length=40)
	fdateofjoin=models.DateField()
	fexp=models.CharField(max_length=40)
	fimg=models.ImageField(upload_to='StaffImages/',default='fa1.jpg')


class Student(models.Model):
	sname=models.CharField(max_length=40)
	sid=models.CharField(max_length=40)
	semail=models.EmailField(max_length=40)
	scourse=models.CharField(max_length=40)
	r = [('m','Male'),('f','Female'),('Df','Select Gender Type')]
	gender=models.CharField(choices=r,default="Df",max_length=12,)
	saddress=models.CharField(max_length=40)
	simg=models.ImageField(upload_to='StudentImages/',default='rgukt.jpg')

class Lfaculty(models.Model):
	lfid=models.CharField(max_length=10)
	y = [('ST','Student'),('FA','Faculty'),('Df','Select')]
	isfaculty=models.CharField(choices=y,default="Df",max_length=12)
	leavefac=models.DateField()

class LStudent(models.Model):
	lstuid=models.CharField(max_length=10)
	n = [('ST','Student'),('FA','Faculty'),('Df','Select')]
	isstudent=models.CharField(choices=n,default="Df",max_length=12)
	leavestu=models.DateField()



class Attendance(models.Model):
    #id=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=40)
    attendedclasses=models.IntegerField()
    totalclasses=models.IntegerField()
    attendance=models.FloatField()
    classestoattend=models.IntegerField()
    
