from django.shortcuts import render
from django.db import models
from django.http import HttpResponse



def index(request):
    return HttpResponse("Olá! Bem vindo ao meu Blog.")
