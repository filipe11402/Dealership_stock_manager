from django.shortcuts import render, redirect
from .models import Carro, Marca, Modelo
from .forms import CreateCarForm, CreateBrandForm, CreateModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def homeview(request):
	cars = Carro.objects.all()
	quantidade = cars.count()

	context = {
		'cars': cars,
		'quantidade': quantidade,
	}
	return render(request, 'stock/index.html', context)


@login_required(login_url='accounts:login')
def create_car_model_view(request):
	form = CreateCarForm()

	if request.method == 'POST':
		form = CreateCarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Stock adicionado com sucesso!')
			return redirect('stock:home')

	context = {
		'form': form,
	}
	return render(request, 'stock/create_car.html', context)


@login_required(login_url='accounts:login')
def edit_carview(request, id):
	car = Carro.objects.get(id=id)
	form = CreateCarForm(instance=car)

	if request.method == 'POST':
		form = CreateCarForm(request.POST, request.FILES, instance=car)
		if form.is_valid():
			form.save()
			messages.success(request, 'Atualizado com sucesso!')
			return redirect('stock:home')

	context = {
		'form': form,
		'car': car,
	}
	return render(request, 'stock/edit_car.html', context)


@login_required(login_url='accounts:login')
def delete_carview(request, id):
	car = Carro.objects.get(id=id)

	if request.method == 'POST':
		car.delete()
		messages.error(request, f'{car} apagado com sucesso!')
		return redirect('stock:home')

	context = {
		'car': car,
	}
	return render(request, 'stock/delete_car.html', context)


@login_required(login_url='accounts:login')
def list_brandview(request):
	brands = Marca.objects.all()
	total_brands = brands.count()

	context = {
		'brands': brands,
		'total_brands': total_brands,
	}
	return render(request, 'stock/list_brands.html', context)


@login_required(login_url='accounts:login')
def create_brandview(request):
	form = CreateBrandForm()

	if request.method == 'POST':
		form = CreateBrandForm(request.POST)
		brand = request.POST.get('marca_carro')
		if form.is_valid():
			form.save()
			messages.success(request, f'{brand} adicionado as marcas disponiveis')
			return redirect('stock:brands')

	context = {
		'form': form,
	}
	return render(request, 'stock/create_brand.html', context)


@login_required(login_url='accounts:login')
def edit_brandview(request, id):
	brand = Marca.objects.get(id=id)
	form = CreateBrandForm(instance=brand)

	if request.method == 'POST':
		form = CreateBrandForm(request.POST, instance=brand)
		if form.is_valid():
			form.save()
			messages.success(request, f'{brand} atualização com sucesso')
			return redirect('stock:brands')

	context = {
		'form': form,
		'brand': brand,
	}
	return render(request, 'stock/edit_brand.html', context)


@login_required(login_url='accounts:login')
def delete_brandview(request, id):
	brand = Marca.objects.get(id=id)


	if request.method == 'POST':
		brand.delete()
		messages.error(request, f'{brand} apagada com sucesso!')
		return redirect('stock:brands')

	context = {
	'brand': brand,
	} 	
	return render(request, 'stock/delete_brand.html', context)


@login_required(login_url='accounts:login')
def list_modelsview(request):
	models = Modelo.objects.all()
	total_models = models.count()


	context = {
		'models': models,
		'total_models': total_models,
	}
	return render(request, 'stock/list_models.html', context)


@login_required(login_url='accounts:login')
def create_modelview(request):
	form = CreateModelForm()

	if request.method == 'POST':
		form = CreateModelForm(request.POST)
		model = request.POST.get('modelo_carro')
		if form.is_valid():
			form.save()
			messages.success(request, f'{model} criado com sucesso!')
			return redirect('stock:models')

	context = {
		'form': form,
	}
	return render(request, 'stock/create_model.html', context)


@login_required(login_url='accounts:login')
def edit_modelview(request, id):
	model = Modelo.objects.get(id=id)
	form = CreateModelForm(instance=model)
	brand = model.marca

	if request.method == 'POST':
		form = CreateModelForm(request.POST, instance=model)
		if form.is_valid():
			form.save()
			messages.success(request, f'{brand} {model} editado com sucesso!')
			return redirect('stock:models')

	context = {
		'model': model,
		'form': form,
	}
	return render(request, 'stock/edit_model.html', context)


@login_required(login_url='accounts:login')
def delete_modelview(request, id):
	model = Modelo.objects.get(id=id)
	brand = model.marca

	if request.method == 'POST':
		model.delete()
		messages.error(request, f'{brand} {model} apagado com sucesso!')
		return redirect('stock:models')

	context = {
		'model': model,
	}
	return render(request, 'stock/delete_model.html', context)
