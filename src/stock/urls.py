from django.urls import path
from .views import *


app_name = 'stock'

urlpatterns = [
	path('', homeview, name='home'),

	## Criar/Editar stock de carros
	path('add-car/', create_car_model_view, name='add-car'),
	path('edit-car/<str:id>/', edit_carview, name='edit-car'),
	path('delete-car/<str:id>/', delete_carview, name='delete-car'),


	## Criar/Editar/Listar/Apagar Marca de carros
	path('brands/', list_brandview, name='brands'),
	path('create-brand/', create_brandview, name='create-brand'),
	path('edit-brand/<str:id>/', edit_brandview, name='edit-brand'),
	path('delete-brand/<str:id>/', delete_brandview, name='delete-brand'),


	## Criar/Editar/Listar/Apagar modelos de carros
	path('models/', list_modelsview, name='models'),
	path('create-model/', create_modelview, name='create-model'),
	path('edit-model/<str:id>/', edit_modelview, name='edit-model'),
	path('delete-model/<str:id>/', delete_modelview, name='delete-model'),
]