from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager


class Empregado(AbstractBaseUser):
	email = models.EmailField(unique=True, max_length=60)
	username = models.CharField(unique=True, max_length=60)
	primeiro_dia = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


	objects = CustomUserManager()


	def __str__(self):
		return self.email

	


	def has_perm(self, perm, obj=None):
		return True


	def has_module_perms(self, app_label):
		return True


