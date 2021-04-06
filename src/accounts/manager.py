from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Necessita de inserir um email')

		if not username:
			raise ValueError('Necessita de inserir um username!')

		user = self.model(email=self.normalize_email(email), username=username)

		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, username, password=None):
		user = self.create_user(email=email, username=username, password=password)

		user.is_staff = True
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


