from django.urls import path
from .views import CommissionListView, CommissionDetailView, CommissionUpdateView, CommissionCreateView


urlpatterns = [
    path('commissions/list', CommissionListView.as_view(), name='commission_list'),
    path('commissions/<int:pk>', CommissionDetailView.as_view(), name='commission_detail'),
    path('commissions/<int:pk>/edit', CommissionUpdateView.as_view(), name='commission_edit'),
    path('commissions/add', CommissionCreateView.as_view(), name='commission_add'),
]


app_name = 'commissions'