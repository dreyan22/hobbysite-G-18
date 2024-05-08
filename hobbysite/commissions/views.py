from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm



class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commission_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['created_commissions'] = Commission.objects.filter(owner=self.request.user.profile)
            context['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=self.request.user.profile).distinct()
        return context
    

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = "commissions/commission_detail.html"

    login_url = '/user/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_owner'] = self.request.user.profile == self.object.owner
        return context


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_form.html'

    def form_valid(self, form):
        self.object = form.save()
        Job.objects.create(
            commission=self.object,
            role=form.cleaned_data['role'],
            manpower_required=form.cleaned_data['manpower_required']
        )
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.pk})

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.pk})


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'commissions/job_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:job_detail', kwargs={'pk': self.object.pk})


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'commissions/job_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:job_detail', kwargs={'pk': self.object.pk})


class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'commissions/jobapplication_form.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.job.commission.pk})