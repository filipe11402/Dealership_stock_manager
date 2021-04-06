from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Marca(models.Model):
	marca_carro = models.CharField(max_length=50)


	def __str__(self):
		return self.marca_carro


class Modelo(models.Model):
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	modelo_carro = models.CharField(max_length=50)


	def __str__(self):
		return self.modelo_carro


class Carro(models.Model):
	modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
	imagem = models.ImageField()
	kilometragem = models.IntegerField()
	ano_registo = models.IntegerField()
	nacional = models.BooleanField(default=True)


	def __str__(self):
		return f'{self.modelo}'


@receiver(pre_delete, sender=Carro)
def apaga_imagem(sender, instance, **kwargs):
	instance.imagem.delete()


