from django.db import models
from django.urls import reverse
from datetime import datetime

from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_OPTIONS = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_OPTIONS, default = 'Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)


    class Meta:
        ordering = [ '-status', 'created_on' ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.pk])


class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    STATUS_OPTIONS = [
        ('Open', 'Open'),
        ('Full', 'Full'),
    ]
    status = models.CharField(max_length=4, choices=STATUS_OPTIONS, default = 'Open')

    class Meta:
        ordering = [ '-status', '-manpower_required', 'role' ]
    
    def __str__(self):
        return self.role


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='applications')
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']

    def __str__(self):
        return f'{self.applicant} - {self.job}'