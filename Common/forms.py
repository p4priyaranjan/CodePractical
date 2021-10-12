from django import forms
from django.db.models import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext, gettext_lazy as _



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['phone_number','email','first_name', 'last_name','user_name' ]
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email','phone_number':'Mobile Number','user_name':'UserName'}

class LoginForm(AuthenticationForm):
    # mobile = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))