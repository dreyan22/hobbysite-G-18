from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('blog/articles',ArticleListView.as_view(), name='article_site'),
    path('blog/article/<int:pk>/',ArticleDetailView.as_view(), name='article'),
]
app_name = 'blog'