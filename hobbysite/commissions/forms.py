from django import forms

from user_management.models import Profile
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ['owner']
        fields = '__all__'
        widgets = {
            'created_on': forms.TextInput(attrs={ 'type': 'datetime-local'}),
            'updated_on': forms.TextInput(attrs={ 'type': 'datetime-local'})
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'