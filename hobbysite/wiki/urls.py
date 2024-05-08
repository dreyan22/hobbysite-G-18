from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, ArticleGalleryView

urlpatterns = [
    path('wiki/articles', ArticleListView.as_view(), name='article_site'),
    path('wiki/article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('wiki/article/<int:pk>/edit', ArticleUpdateView.as_view(), name='update'),
    path('wiki/article/add', ArticleCreateView.as_view(), name='create'),
    path('wiki/article/<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('wiki/article/gallery', ArticleGalleryView.as_view(), name='gallery'),
]

app_name = 'wiki'