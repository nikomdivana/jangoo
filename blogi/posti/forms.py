from django import forms
from .models import posti

class PostForm(forms.ModelForm):
    class Meta:
        model = posti
        fields = ['name']
