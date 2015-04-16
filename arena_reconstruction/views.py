from arena_reconstruction.models import Course, Class, Teacher
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
	return render(request, "home.html", {"activeTab":"home"})

def course1(request):
	courseId=1
	showClass(courseId)
	return render(request, "course1.html", {"activeTab":"course1", "classes":Class.objects.all()})
	

def course2(request):
	return render(request, "course2.html", {"activeTab":"course2"})
	

def course3(request):
	return render(request, "course3.html", {"activeTab":"course3"})
	

def course4(request):
	return render(request, "course4.html", {"activeTab":"course4"})
	

def course5(request):
	return render(request, "course5.html", {"activeTab":"course5"})
	

def course6(request):
	return render(request, "course6.html", {"activeTab":"course6"})
	

def course7(request):
	return render(request, "course7.html", {"activeTab":"course7"})

def final(request):
	return render(request, "final.html", {"activeTab":"final"})

