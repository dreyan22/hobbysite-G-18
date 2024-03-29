from django.urls import path

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('wiki/articles', ArticleListView.as_view(), name='article_site'),
    path('wiki/article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
]

app_name = 'wiki'