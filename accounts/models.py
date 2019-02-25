from django.contrib import auth
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class User(auth.models.User, auth.models.PermissionsMixin):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	def __str__(self):
		return self.username