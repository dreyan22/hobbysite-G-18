from django.shortcuts import render, redirect
from .models import Product, Transaction, Profile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from django.urls import reverse

class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            try:
                user_profile = Profile.objects.get(user=user)
                user_products = Product.objects.filter(owner=user_profile)
                context['user_products'] = user_products
                context['products'] = Product.objects.exclude(owner=user_profile)
            except Profile.DoesNotExist:
                # Create a profile for the user if it doesn't exist
                Profile.objects.create(user=user)
                context['products'] = Product.objects.all()
        else:
            context['products'] = Product.objects.all()
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"
    login_url = '/user/login/'
    form_class = TransactionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        user = self.request.user
        if user.is_authenticated and product.owner != user.profile:
            context['transaction_form'] = TransactionForm(initial={'product': product})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()  # Ensure to call get_form method here
        product = self.object
        if form.is_valid():
            if product.stock > 0:
                transaction = form.save(commit=False)
                transaction.buyer = request.user.profile
                transaction.product = product
                transaction.status = 'On cart'
                transaction.save()
                product.stock -= transaction.amount 
                product.update_status() 
                product.save()
                return self.form_valid(form)
            else:
                form.add_error(product.update_status, "Product is out of stock.")
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse('merchstore:cart')
        else:
            return reverse('login')

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'product_type', 'description', 'price', 'stock', 'status']
    template_name = "merchstore/product_add.html"
    login_url = '/user/login/'

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
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

class CartView(ListView):
    model = Transaction
    template_name = "merchstore/cart.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile, status='On cart').order_by('product__owner')

class TransactionListView(ListView):
    model = Transaction
    template_name = "merchstore/transactions.html"
    login_url = '/user/login/'

    def get_queryset(self):
        return Transaction.objects.filter(product__owner=self.request.user.profile).order_by('buyer')