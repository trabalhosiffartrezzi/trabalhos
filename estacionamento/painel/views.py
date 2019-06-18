from django.shortcuts import render
from django.db import models
from django.http import HttpResponse



def index(request):
    return render(request, 'painel/index.html')
