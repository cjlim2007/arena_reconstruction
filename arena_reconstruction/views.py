from arena_reconstruction.models import Course, Class, Teacher
from django.shortcuts import render
import logging

courseId=1
def showClass(request):
	showclasses=Class.objects.all().filter(course=courseId)
	# showclasses="hi"
	return render (request,"temp.html",{"classes":showclasses})

