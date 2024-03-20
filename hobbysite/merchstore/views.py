from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"