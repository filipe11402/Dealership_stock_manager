from django.forms import ModelForm
from .models import Carro, Marca, Modelo


class CreateCarForm(ModelForm):
	class Meta:
		model = Carro
		fields = '__all__'

class CreateBrandForm(ModelForm):
	class Meta:
		model = Marca
		fields = '__all__'


class CreateModelForm(ModelForm):
	class Meta:
		model = Modelo
		fields = '__all__'