from django.contrib.auth.forms import UserCreationForm
from .models import Empregado


class RegisterUserForm(UserCreationForm):
	class Meta:
		model = Empregado
		fields = ['email', 'username', 'password1', 'password2']