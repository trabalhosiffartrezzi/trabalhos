from django import forms
from django.utils import timezone


class FormLogin(forms.Form):
	usuario = forms.CharField(label="Usuário", max_length=20) 	
	senha = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)   

class FormVaga(forms.Form):
	rua = forms.CharField(max_length=200)
	bairro = forms.CharField(max_length=100)
	referencia = forms.CharField(widget=forms.Textarea, max_length=200)
	cidade = forms.CharField(max_length=100)
	estado = forms.CharField(max_length=2)
	valor = forms.IntegerField(initial=0.00)
	categoria = forms.CharField(max_length=100)
	rascunho = forms.BooleanField(required=True)
	