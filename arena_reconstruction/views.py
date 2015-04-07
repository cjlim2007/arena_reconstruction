from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

def home(request):
    return render(request, "home.html")

def course1(request):
	return render(request, "course1.html")

def course2(request):
	return render(request, "course2.html")

def course3(request):
	return render(request, "course3.html")

def course4(request):
	return render(request, "course4.html")

def course5(request):
	return render(request, "course5.html")

def course6(request):
	return render(request, "course6.html")

def course7(request):
	return render(request, "course7.html")

def final(request):
	return render(request, "final.html")