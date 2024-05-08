from django import forms

from user_management.models import Profile
from .models import Commission

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        widgets = {
            'created_on': forms.TextInput(attrs={ 'type': 'datetime-local'}),
            'updated_on': forms.TextInput(attrs={ 'type': 'datetime-local'})
        }
