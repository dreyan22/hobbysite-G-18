from django.contrib import admin

from .models import ArticleCategory, Article

class ArticleInline(admin.TabularInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    model = [ArticleInline]

admin.site.register(ArticleCategory, ArticleAdmin)
admin.site.register(Article)
