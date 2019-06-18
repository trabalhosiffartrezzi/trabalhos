from django import forms
from django.utils import timezone


class FormLogin(forms.Form):
   usuario = forms.CharField(label="Usuário", max_length=20) 
   senha = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)   