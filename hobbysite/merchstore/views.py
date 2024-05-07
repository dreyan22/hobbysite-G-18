from django.shortcuts import render
from .models import Product, Transaction
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
    login_url = '/user/login/'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    template_name = "merchstore/product_add.html"
    login_url = '/user/login/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    template_name = "merchstore/product_edit.html"
    login_url = '/user/login/'


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile, status='On cart')
    

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/transactions.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile)