from django import forms
from .models import comments

class commentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment',]