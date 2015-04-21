from arena_reconstruction.models import Course, Class, Teacher
from django.shortcuts import render
import logging
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from pprint import pprint

# with open('arena_reconstruction/fixtures/fakeData.json') as data_file:    
# 		data = json.loads(data_file.read())
# 		for i in data:
# 			printIt=Course.o
# courseId=1
def showClass(request):

	# showSelectedCourse=Class.objects.all().filter(course=courseId)
		# showclasses="hi"
	return render (request,"temp.html",{"classes":Class.objects.all()})

@login_required
def home(request):
    return render(request, "home.html", {"activeTab":"home"})

@login_required
def course1(request):
	return render(request, "course1.html", {"activeTab":"course1"})
	
@login_required
def course2(request):
	return render(request, "course2.html", {"activeTab":"course2"})
	
@login_required
def course3(request):
	return render(request, "course3.html", {"activeTab":"course3"})
	
@login_required
def course4(request):
	return render(request, "course4.html", {"activeTab":"course4"})
	
@login_required
def course5(request):
	return render(request, "course5.html", {"activeTab":"course5"})
	
@login_required
def course6(request):
	return render(request, "course6.html", {"activeTab":"course6"})
	
@login_required
def course7(request):
	return render(request, "course7.html", {"activeTab":"course7"})

@login_required
def final(request):
	return render(request, "final.html", {"activeTab":"final"})

def successfully_logged_out(request):
	return render(request, "registration/logout.html")
