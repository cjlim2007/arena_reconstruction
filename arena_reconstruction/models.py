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

class Studentcourse(models.Model):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=255)
    