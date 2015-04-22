from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

# class Subject(models.Model):
#     name = models.CharField(max_length=255)

class Class(models.Model):
    block = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    teacher = models.ForeignKey('arena_reconstruction.Teacher')
    course = models.ForeignKey('arena_reconstruction.Course')

class Schedule(models.Model):
	user = models.ForeignKey('auth.User')
	class1 = models.ForeignKey('arena_reconstruction.Class', related_name='class1', blank = True)
	class2 = models.ForeignKey('arena_reconstruction.Class', related_name='class2', blank = True)
	class3 = models.ForeignKey('arena_reconstruction.Class', related_name='class3', blank = True)
	class4 = models.ForeignKey('arena_reconstruction.Class', related_name='class4', blank = True)
	class5 = models.ForeignKey('arena_reconstruction.Class', related_name='class5', blank = True)
	class6 = models.ForeignKey('arena_reconstruction.Class', related_name='class6', blank = True)
	class7 = models.ForeignKey('arena_reconstruction.Class', related_name='class7', blank = True)
	#class8 = models.ForeignKey('arena_reconstruction.Class', related_name='class8', required = False)
#milo distracted us with stupid slogans and now we are stuck here. plz help
