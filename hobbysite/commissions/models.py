from django.db import models
from django.urls import reverse
from datetime import datetime


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


    class Meta:
        ordering = [ 'created_on' ]
    
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
