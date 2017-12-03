from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .models import Job, Student, StudentJob


class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "deadline",
        "whether_approved",
    ]
    ordering = ["deadline"]
    search_fields = ['title']
    list_filter = ["hours", "deadline", "whether_approved"]

    actions = ["approve_jobs"]
    def approve_jobs(self, request, queryset):
        num_approved = queryset.update(whether_approved="yes")
        if num_approved == 1:
            message_bit = "1 job was"
        else:
            message_bit = "%s jobs were" % num_approved
        self.message_user(request, "%s successfully approved." % message_bit)
    approve_jobs.short_description = "Approve selected jobs"

    def disapprove_jobs(self, request, queryset):
        num_disapproved = queryset.update(whether_approved="no")
        if num_disapproved == 1:
            message_bit = "1 job was"
        else:
            message_bit = "%s jobs were" % num_disapproved
        self.message_user(request, "%s successfully disapproved." % message_bit)
    disapprove_jobs.short_description = "Disapprove selected jobs"


class StudentJobAdmin(admin.ModelAdmin):
    
    def sort_applicants(self, obj):
        pass
                

class StudentAdmin(admin.ModelAdmin):
	pass


admin.site.register(Job, JobAdmin)
admin.site.register(StudentJob, StudentJobAdmin)
admin.site.register(Student, StudentAdmin)
