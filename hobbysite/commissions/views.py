from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Commission
from .forms import CommissionForm



class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commission_list.html"
    
    logout_url = '/commissions/list'


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"

    login_url = '/user/login/'


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.pk})

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.pk})
