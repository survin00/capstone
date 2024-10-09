from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUserAccManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class UserAcc(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=100, unique=True)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateField(auto_now_add=True)
	phone = models.CharField(max_length=13, blank=True, null=True)
	USERNAME_FIELD = 'email'
	#REQUIRED_FIELDS = ['firstname','lastname']
	objects = CustomUserAccManager()

	def __str__(self):
		return self.email