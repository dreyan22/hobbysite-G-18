from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    model = Job


class JobApplicationInline(admin.TabularInline):
    model = JobApplication


class JobAdmin(admin.ModelAdmin):
    inlines = [JobApplicationInline]
    list_display = ['role', 'manpower_required', 'status']
    ordering = ['-status', '-manpower_required', 'role']


class CommissionAdmin(admin.ModelAdmin):
    inlines = [JobInline]
    list_display = ['title', 'description', 'status', 'created_on', 'updated_on']
    ordering = ['created_on']


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication)

