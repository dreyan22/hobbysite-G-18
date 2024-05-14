from django.urls import path
from .views import CommissionListView, CommissionDetailView, CommissionUpdateView, CommissionCreateView, JobCreateView, JobUpdateView, JobApplicationCreateView


urlpatterns = [
    path('commissions/list', CommissionListView.as_view(), name='commission_list'),
    path('commissions/<int:pk>', CommissionDetailView.as_view(), name='commission_detail'),
    path('commissions/<int:pk>/edit', CommissionUpdateView.as_view(), name='commission_edit'),
    path('commissions/add', CommissionCreateView.as_view(), name='commission_add'),
    path('jobs/add', JobCreateView.as_view(), name='job_add'),
    path('jobs/<int:pk>/edit', JobUpdateView.as_view(), name='job_edit'),
    path('jobs/<int:pk>/apply', JobApplicationCreateView.as_view(), name='job_apply'),
]


app_name = 'commissions'