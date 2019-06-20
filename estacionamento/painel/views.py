from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Vaga
from .forms import FormLogin
from .forms import FormVaga
from datetime import datetime 
from django.http import HttpResponse   
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'painel/index.html')

def vagas(request):
	
	lista_vagas = Vaga.objects.all()
	contexto = {'lista_vagas': lista_vagas}
	return render(request, 'painel/vagas.html', contexto)


def autenticar(request):
   if request.method == 'POST':
      #Tratar os dados vindos do formulário
      form = FormLogin(request.POST)
      if form.is_valid():
         username = form.cleaned_data['usuario']
         senha = form.cleaned_data['senha']
         
         #Autenticar
         usuario = authenticate(request, username=username, password=senha)
         if usuario is not None:
            login(request, usuario) #Mantém o usuário logado
            return HttpResponseRedirect('/painel/meuperfil')
         else:
            contexto = {"form": form, "mensagem": "Usuário ou senha inválida" }
            return render(request, 'painel/index.html', contexto)
      else:
         return HttpResponse("Formulário inválido")
   else:
      #Exibir o formulário (Vindo do GET)
      form = FormLogin()
      contexto = {"form": form}
      return render(request, 'painel/index.html', contexto)

def meuperfil(request):
	return render(request, 'painel/meuperfil.html')

def sair(request):
   logout(request)
   return HttpResponseRedirect('/painel/')

def cadastravaga(request):
   if request.method == 'POST':
      form = FormVaga(request.POST)
      if form.is_valid():
         v = Vaga() 
         v.dono = request.user
         v.rua = form.cleaned_data['rua']
         v.bairro = form.cleaned_data['bairro']
         v.referencia = form.cleaned_data['referencia']
         v.cidade = form.cleaned_data['cidade']
         v.estado = form.cleaned_data['estado']
         v.valor = form.cleaned_data['valor']
         v.categoria = form.cleaned_data['categoria']
         v.save()
         return HttpResponseRedirect('/painel/meuperfil')
      else:
         return HttpResponse("Formulário inválido")
   else:
      form = FormVaga()
      contexto = {"form": form}
      return render(request, 'painel/cadastravaga.html', contexto)