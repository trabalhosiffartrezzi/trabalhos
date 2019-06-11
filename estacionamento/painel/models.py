from django.db import models
from django.utils import timezone

class Vaga(models.Model):
	Rua = models.CharField(max_length=50)
	Bairro = models.CharField(max_length=50)
	Referencia = models.CharField(max_length=200)
	Cidade = models.CharField(max_length=50)
	Estado = models.CharField(max_length=2)
	Valor = models.FloatField(default=0.00)
	

