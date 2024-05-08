from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, CartView, TransactionListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('merchstore/items', ProductListView.as_view(), name='product_list_redirect'),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('merchstore/item/add', ProductCreateView.as_view(), name='product_add'),
    path('merchstore/item/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('merchstore/cart', CartView.as_view(), name='cart'),
    path('merchstore/transactions', TransactionListView.as_view(), name='transactions'),
]

app_name = 'merchstore'