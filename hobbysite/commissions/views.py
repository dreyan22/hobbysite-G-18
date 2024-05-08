from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Commission


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commission_list.html"
    
    logout_url = '/commissions/list'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"

    login_url = '/user/login/'

