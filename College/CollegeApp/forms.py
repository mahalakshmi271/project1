#from django.forms import ModelForm
from CollegeApp.models import Faculty,Student,Lfaculty,LStudent,Attendance,User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class Fform(forms.ModelForm):
	class Meta:
		model=Faculty
		fields = ["fname","feducation","fdep","femail","faddress","fdateofjoin","fexp","fimg"]
		widgets = {
		"fname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Faculty Name",
			}),
		"feducation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Faculty Education",
			}),
		"fdep":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Faculty Department",
			
			}),
		"femail":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Faculty Email",
			
			}),
		
		"faddress":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":3,
			}),
		"fdateofjoin":forms.DateInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Date of Join",
			"type":"Date",
			
			}),
		"fexp":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Experience",
			
			}),


		}



class Sform(forms.ModelForm):
	class Meta:
		model=Student
		fields = ["sname","sid","semail","scourse","gender","saddress","simg"]
		widgets = {
		"sname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Name",
			}),
		"sid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Id",
			}),
		"semail":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Email",
			
			}),
		"scourse":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Course",
			
			}),
		
		"gender":forms.Select(attrs={
			"class":"form-control my-2",
			
			
			}),
		"saddress":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Address",
			"rows":3,
			
			}),
		


		}


class Lform(forms.ModelForm):
	class Meta:
		model=Lfaculty
		fields = ["lfid","isfaculty","leavefac"]
		widgets = {
		"lfid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Faculty Id",
			}),

		"isfaculty":forms.Select(attrs={
			"class":"form-control my-2",
			
			}),
		
		"leavefac":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"Date",
			}),
		}


class SLform(forms.ModelForm):
	class Meta:
		model=LStudent
		fields = ["lstuid","isstudent","leavestu"]
		widgets = {
		"lstuid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Id",
			}),

		"isstudent":forms.Select(attrs={
			"class":"form-control my-2",
			
			}),
		
		"leavestu":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"Date",
			}),
		}


class SAform(forms.ModelForm):
	class Meta:
		model=Attendance
		fields = ["id","coursename","attendedclasses","totalclasses","attendance","classestoattend"]
		widgets = {
		#"id":forms.NumberInput(attrs={
			#"class":"form-control my-2",
			#"placeholder":"Enter Student Id",
			#}),
		"coursename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Course Name",
			}),
		"attendedclasses":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Attended Classes",
			}),
		"totalclasses":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Total Classes",
			}),
		"attendance":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Attendance",
			}),
		"classestoattend":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Classes Toatl Attend",
			}),
		}




class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Password",
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}






	
