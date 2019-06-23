from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('vagas', views.vagas, name='vagas'),
    path('autenticar', views.autenticar, name='autenticar'),
    path('meuperfil', views.meuperfil, name='meuperfil'),
    path('sair', views.sair, name='sair'),
    path('cadastravaga', views.cadastravaga, name='cadastravaga'),
    path('adicional', views.adicional, name='adicional'),
    url('fotos', views.fotos, name='fotos'),



    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)