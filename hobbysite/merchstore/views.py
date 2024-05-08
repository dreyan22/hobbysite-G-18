from django.shortcuts import render, redirect
from .models import Product, Transaction
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm

class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            user_products = Product.objects.filter(owner=user.profile)
            context['user_products'] = user_products
            context['products'] = Product.objects.exclude(owner=user.profile)
        else:
            context['products'] = Product.objects.all()
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
    login_url = '/user/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        user = self.request.user
        if user.is_authenticated and product.owner != user.profile:
            context['transaction_form'] = TransactionForm(initial={'product': product})
        return context

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = request.user.profile
            transaction.save()
            return redirect('merchstore:cart')
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    template_name = "merchstore/product_add.html"
    login_url = '/user/login/'

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    template_name = "merchstore/product_edit.html"
    login_url = '/user/login/'

    def form_valid(self, form):
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = 'Out of stock'
        else:
            product.status = 'Available'
        product.save()
        return super().form_valid(form)

class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile, status='On cart').order_by('product__owner')

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/transactions.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile).order_by('buyer')