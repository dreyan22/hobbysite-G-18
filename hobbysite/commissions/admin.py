from django.contrib import admin

from .models import Commission, Job


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    inlines = [JobInline]
    list_display = ['title', 'description', 'status', 'created_on', 'updated_on']
    ordering = ['created_on']


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job)

