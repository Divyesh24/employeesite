from django import forms
from .models import EmpInfo

class InfoForm(forms.ModelForm):
    
    class Meta:
        model = EmpInfo
        fields = ('firstName', 'lastName','email','mobileNumber','salary')
        