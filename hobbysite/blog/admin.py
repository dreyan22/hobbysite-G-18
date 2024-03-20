from django.contrib import admin

# Register your models here.
from .models import Article, ArticleCategory

class ArticleInline(admin.StackedInline):
    model = Article
     
class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article)
