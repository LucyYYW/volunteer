from django.db import models

class Student(models.Model):
	name = models.CharField()
	number = models.CharField(max_length=8)
	password = models.CharField(max_length=8)

	male = 'M'
	female = 'F'
	sex_choices = (
		(male, 'male')
		(female, 'female')
	)
	sex = models.CharField(
		max_length=2,
		choices = sex_choices,
		default = male
	)

	hours_got = models.IntergerField()
	misconduct = models.BooleanField()
	GPA_ranking = models.IntergerField()



class Student_job(models.Model):
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
	status = models.IntergerField(
		choices = status_choices,
		default = Applied
	)

	written_info = models.CharField(max_length = 200)



class Teacher(models.Model):
	user = models.CharField()
	password = models.CharField(max_length=8)


class Club(models.Model):
	name = models.CharField()
	number = models.CharField(max_length=8)
	password = models.CharField(max_length=8)


class Job(models.Model):
	club = models.ForeignKey('Club')
	title = models.CharField()
	location = models.CharField()
	time = models.DateTimeField()
	hours = models.IntergerField()
	deadline = models.DateTimeField()
	additional_info = models.CharField(max_length=200)
	whether_approved = models.BooleanField(default=True)