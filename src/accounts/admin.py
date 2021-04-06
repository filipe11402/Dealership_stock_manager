from django.contrib import admin
from .models import Empregado
from django.contrib.auth.admin import UserAdmin


class EmpregadoAdmin(UserAdmin):
	list_display = ('email', 'username', 'primeiro_dia', 'is_active', 'is_admin', 'is_staff',)
	readonly_fields = ('primeiro_dia', 'last_login',)
	search_fields = ('email', 'username',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Empregado, EmpregadoAdmin)

