from django.contrib import admin
from .models import Job, StudentJob


class JobAdmin(admin.ModelAdmin):
	list_display = [
		"title",
		"deadline",
		"whether_approved",
	]
	search_fields = ['title']
	list_filter = ["hours", "deadline", "whether_approved"]


class StudentJobAdmin(admin.ModelAdmin):
	pass		


admin.site.register(Job, JobAdmin)
admin.site.register(StudentJob, StudentJobAdmin)
