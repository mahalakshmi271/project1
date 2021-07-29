from django.shortcuts import render,redirect
from django.http import HttpResponse
from CollegeApp.forms import Fform,Sform,Lform,SLform,SAform,UsgForm
from CollegeApp.models import Faculty,Student,Lfaculty,LStudent,Attendance,User
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from django.contrib import messages
#from CollegeApp import settings

# Create your views here.


def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

@login_required
def factlist(request):
	y = Faculty.objects.all()
	if request.method == "POST":
		t = Fform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Faculty Added successfully")
			return redirect('/flist')
	t = Fform()
	
	return render(request,'html/facultylist.html',{'q':t,'a':y})

@login_required
def factup(request,m):
	k = Faculty.objects.get(id=m)
	if request.method == "POST":
		e = Fform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Faculty Updated successfully".format(k.fname))
			return redirect('/flist')
	e = Fform(instance=k)
	return render(request,'html/factupdate.html',{'x':e})

@login_required
def factdl(request,n):
	v = Faculty.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/flist')
	return render(request,'html/factdlt.html',{'q':v})

@login_required
def factvw(request,a):
	s = Faculty.objects.get(id=a)
	return render(request,'html/facview.html',{'z':s})


@login_required
def stulist(request):
	y = Student.objects.all()
	if request.method == "POST":
		t= Sform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Student Added successfully")
			return redirect('/slist')
	t = Sform()
	return render(request,'html/studentlist.html',{'q':t,'a':y})



@login_required
def stuup(request,m):
	k = Student.objects.get(id=m)
	if request.method == "POST":
		e = Sform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Faculty Updated successfully".format(k.sname))
			return redirect('/slist')
	e = Sform(instance=k)
	
	return render(request,'html/studentupdate.html',{'x':e})

@login_required
def studl(request,n):
	v = Student.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/slist')
	return render(request,'html/studentdelete.html',{'q':v})

@login_required
def stuvw(request,a):
	s = Student.objects.get(id=a)
	return render(request,'html/studentview.html',{'z':s})

@login_required
def lelist(request):
	y = Lfaculty.objects.all()
	if request.method == "POST":
		t= Lform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Faculty Leave Added successfully")
			return redirect('/llist')
	t = Lform()
	return render(request,'html/leavelist.html',{'q':t,'a':y})

@login_required
def lfacup(request,m):
	k = Lfaculty.objects.get(id=m)
	if request.method == "POST":
		e = Lform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Faculty Leave Updated successfully".format(k.lfid))
			return redirect('/llist')
	e = Lform(instance=k)
	return render(request,'html/factleaveupdate.html',{'x':e})

@login_required
def fldl(request,n):
	v = Lfaculty.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/llist')
	return render(request,'html/facultyleavedelete.html',{'q':v})



@login_required
def flvw(request,a):
	s = Lfaculty.objects.get(id=a)
	return render(request,'html/facultyleaveview.html',{'z':s})



@login_required
def studentlist(request):
	y = LStudent.objects.all()
	if request.method == "POST":
		t= SLform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Faculty Leave Added successfully")
			return redirect('/stulist')
	t = SLform()
	return render(request,'html/studentleavelist.html',{'q':t,'a':y})

@login_required
def stulup(request,m):
	k = LStudent.objects.get(id=m)
	if request.method == "POST":
		e = SLform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Faculty Leave Updated successfully".format(k.lstuid))
			return redirect('/stulist')
	e = SLform(instance=k)
	
	return render(request,'html/studentleaveupdate.html',{'x':e})

@login_required
def stuldl(request,n):
	v = LStudent.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/stulist')
	return render(request,'html/studentleavedelete.html',{'q':v})

@login_required
def stulvw(request,a):
	s = LStudent.objects.get(id=a)
	return render(request,'html/studentleaveview.html',{'z':s})


@login_required
def stuattendlist(request):
	y = Attendance.objects.all()
	if request.method == "POST":
		t= SAform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Student Attendance Added successfully")
			return redirect('/stuatlist')
	t = SAform()
	return render(request,'html/studentattenancelist.html',{'q':t,'a':y})



@login_required
def stauup(request,m):
	k = Attendance.objects.get(id=m)
	if request.method == "POST":
		e = SAform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Student Attendance Updated successfully".format(k.coursename))
			return redirect('/stuatlist')
	e = SAform(instance=k)
	
	return render(request,'html/studenattendanceupdate.html',{'x':e})


@login_required
def stualdl(request,n):
	v = Attendance.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/stuatlist')
	return render(request,'html/studentattendancedelete.html',{'q':v})


@login_required
def stuavw(request,a):
	s = Attendance.objects.get(id=a)
	return render(request,'html/studentattendanceview.html',{'z':s})



@login_required
def feedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sm = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'html/feedback.html')



def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'html/usrregister.html',{'t':d})






