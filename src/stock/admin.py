from django.contrib import admin
from .models import Marca, Modelo, Carro


class CarroAdmin(admin.ModelAdmin):
	list_display = ('modelo', 'kilometragem', 'ano_registo', 'nacional')


admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Carro, CarroAdmin)