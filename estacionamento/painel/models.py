from django.db import models
from django.utils import timezone

class Vaga(models.Model):
	dono = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="")
	rua = models.CharField(max_length=50)
	bairro = models.CharField(max_length=50)
	referencia = models.CharField(max_length=200)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2)
	valor = models.FloatField(default=0.00)
	categoria = models.TextField(default="")
	rascunho = models.BooleanField(default=True)

	def __str__(self):
		return str(self.dono) + " - " + self.rua + " - " + str(self.valor)  


class Foto(models.Model):
	vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE) 
	descricao = models.TextField()
	imagens = models.ImageField(upload_to='images/', default="")

	def __str__(self):
		return str(self.vaga) + " - " + self.descricao
	

