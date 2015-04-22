from arena_reconstruction.models import Course, Class, Teacher, Studentcourse
from django.shortcuts import render
import logging
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from pprint import pprint

# with open('arena_reconstruction/fixtures/fakeData.json') as data_file:    
# 		data = json.loads(data_file.read())
# 		for i in data:
# 			printIt=Course.o
# courseId=1
def showClass(courseId):
	showSelectedCourse=Class.objects.all().filter(course=courseId)
		# showclasses="hi"
	# return render (request,"temp.html",{"classes":Class.objects.all()})


def home(request):
	return render(request, "home.html", {"activeTab":"home", "studentCourses":Studentcourse.objects.all()})

def course1(request):
	courseId=1
	showClass(courseId)

	return render(request, "course1.html", {"activeTab":"course1", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course2(request):
	courseId=2
	return render(request, "course2.html", {"activeTab":"course2", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course3(request):
	courseId=3
	return render(request, "course3.html", {"activeTab":"course3", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course4(request):
	courseId=4
	return render(request, "course4.html", {"activeTab":"course4", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course5(request):
	courseId=5
	return render(request, "course5.html", {"activeTab":"course5", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course6(request):
	courseId=6
	return render(request, "course6.html", {"activeTab":"course6", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})
	

def course7(request):
	courseId=7
	return render(request, "course7.html", {"activeTab":"course7", "classes":Class.objects.all().filter(course=courseId), "studentCourses":Studentcourse.objects.all()})

def final(request):
	return render(request, "final.html", {"activeTab":"final", "studentCourses":Studentcourse.objects.all()})

# def showTab1(request):
# 	return render(request, "base.html", {})

# def showTab2(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.second()})

# def showTab3(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.third()})

# def showTab4(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.fourth()})

# def showTab5(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.fifth()})

# def showTab6(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.sixth()})

# def showTab7(request):
# 	return render(request, "base.html", {"Studentcourse": Studentcourse.objects.seventh()})


