from django import forms
from .models import Lead

class LeadCreateForm(forms.ModelForm):
    class Meta:
        fields = ("first_name", "last_name", "age", "description", "agent")
        model = Lead


