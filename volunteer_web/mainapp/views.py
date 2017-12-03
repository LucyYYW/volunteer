from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.

def index(request):
	if "firstname" in request.POST:
		queryset = Student.objects.filter(student_number=request.POST['firstname'])
		for student in queryset:
			student.hours_got = 1
			student.save()
		return HttpResponse("Welcome " + str(request.POST['firstname']))
	else:
		return HttpResponse("Welcome!")

def test_form(request):
	context = {}
	return render(request, 'sampleform.html', context)
