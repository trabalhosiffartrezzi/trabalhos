from django.urls import path
from . import views

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('vagas', views.vagas, name='vagas'),
    path('autenticar', views.autenticar, name='index'),
    path('meuperfil', views.meuperfil, name='meuperfil'),
    path('sair', views.sair, name='sair'),


    ]