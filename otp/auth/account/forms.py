from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
class LoginForm(forms.Form):
    phone=forms.IntegerField(label='Your Phone Number')
    password=forms.CharField(widget= forms.PasswordInput)
    
class VerifyForm(forms.Form):
    key=forms.IntegerField(label='Please enter your OTP here')


