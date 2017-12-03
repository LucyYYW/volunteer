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

	class Meta:
		verbose_name = 'Student'
		verbose_name_plural = 'Students'

	def __str__(self):
		return self.student_number


class StudentJob(models.Model):
	student = models.ForeignKey('Student')
	job = models.ForeignKey('Job')

	status_choices = (
		("applied", "applied"),
		("approved", "approved"),
		("disapproved", 'disapproved'),
		("finished", "finished")
	)
	status = models.CharField(
		choices=status_choices,
		max_length = 20,
		default="applied",
	)

	written_info = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return str(self.student.student_number) + " " + str(self.job.title)

	def student_ranking(self):
		return self.student.GPA_ranking
	student_ranking.admin_order_field = 'student__GPA_ranking'


class Teacher(User):
	pass


class Club(User):
	club_number = models.CharField(max_length=8)
	
	class Meta:
		verbose_name = 'Club'
		verbose_name_plural = 'Clubs'

	def __str__(self):
		return self.club_number


class Job(models.Model):
	club = models.ForeignKey('Club')
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	time = models.DateTimeField()
	hours = models.IntegerField(blank=True, null=True)
	deadline = models.DateTimeField()
	additional_info = models.CharField(max_length=200, blank=True, null=True)
	total = models.IntegerField(blank=True, null=True)
	
	whether_approved_choices = (
		("unknown",'unknown'),
		("yes","approved"),
		("no","no"),
	)
	whether_approved = models.CharField(choices=whether_approved_choices, max_length = 10, default="unknown")
	
	class Meta:
		verbose_name = 'Job'
		verbose_name_plural = 'Jobs'

	def __str__(self):
		return self.title

