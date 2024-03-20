from django.contrib import admin

from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'description', 'people_required', 'created_on', 'updated_on']
    ordering = ['created_on']


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment)

