from django.db import models
from django.contrib.auth.models import User


class Student(User):
	student_number = models.CharField(max_length=8)

	male = 'M'
	female = 'F'
	sex_choices = [
		(male, 'male'),
		(female, 'female'),
	]
	sex = models.CharField(
		max_length=2,
		choices=sex_choices,
		default=male,
	)

	hours_got = models.IntegerField()
	misconduct = models.BooleanField()
	GPA_ranking = models.IntegerField()


class StudentJob(models.Model):
	student = models.ForeignKey('Student')
	job = models.ForeignKey('Job')

	Applied = 1
	Approved = 2
	Unapproved = 3
	Finished = 4
	status_choices = (
		(Applied, "applied"),
		(Approved, "approved"),
		(Unapproved, 'unapproved'),
		(Finished, "finished")
	)
	status = models.IntegerField(
		choices=status_choices,
		default=Applied,
	)

	written_info = models.CharField(max_length=200, blank=True, null=True)


class Teacher(User):
	pass


class Club(User):
	club_number = models.CharField(max_length=8)


class Job(models.Model):
	club = models.ForeignKey('Club')
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	time = models.DateTimeField()
	hours = models.IntegerField(blank=True, null=True)
	deadline = models.DateTimeField()
	additional_info = models.CharField(max_length=200, blank=True, null=True)
	whether_approved = models.BooleanField(default=True)
