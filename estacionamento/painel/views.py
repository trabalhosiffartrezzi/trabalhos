from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Vaga



def index(request):
    return render(request, 'painel/index.html')

def vagas(request):
	
	lista_vagas = Vaga.objects.all()
	contexto = {'lista_vagas': lista_vagas}
	return render(request, 'painel/vagas.html', contexto)