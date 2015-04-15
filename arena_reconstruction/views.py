from arena_reconstruction.models import Course, Class, Teacher
from django.shortcuts import render
import logging
import json

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
