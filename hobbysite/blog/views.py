from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article
    
class ArticleListView(ListView):
    model = Article
    template_name = 'article_site.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_main'] = True  
        return context
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_main'] = False  # Set to False since it's not the main page
        return context
    
    


 
# Create your views here.
