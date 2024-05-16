from django.contrib import admin

from .models import ArticleCategory, Article, Comment

class ArticleInline(admin.StackedInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['author_username', 'article_title']

admin.site.register(ArticleCategory, ArticleAdmin)
admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)