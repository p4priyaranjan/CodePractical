from django import forms
from .models import UserFile

class UserFileForm(forms.ModelForm):
    class Meta:
        model=UserFile
        fields=['my_file']
        