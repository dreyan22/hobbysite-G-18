from django import forms

from user_management.models import Profile
from .models import Commission, Job, JobApplication
from django.forms import inlineformset_factory


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'


class CommissionForm(forms.ModelForm):
    role = forms.CharField(max_length=255)
    manpower_required = forms.IntegerField()
    class Meta:
        # exclude = ['owner']
        model = Commission
        fields = '__all__'
        JobFormSet = inlineformset_factory(Commission, Job, form=JobForm, extra=1)
        widgets = {
            'created_on': forms.TextInput(attrs={ 'type': 'datetime-local'}),
            'updated_on': forms.TextInput(attrs={ 'type': 'datetime-local'}),
        }