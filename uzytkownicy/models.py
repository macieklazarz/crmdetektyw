from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid
from django.urls import reverse

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	imie = models.TextField(max_length=60, null=False)
	nazwisko = models.TextField(max_length=60, null=False)
	adres = models.TextField(max_length=60, null=False)
	email = models.EmailField(_("Adres email"), unique=True)
	numer_telefonu = models.CharField(max_length=20, help_text='Numer telefonu')
	inne = models.TextField(max_length=1024, blank=True, null=True)
	admin = models.BooleanField(default=False)
	detektyw = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		if self.detektyw:
			url = 'staff_update'
		else:
			url = 'customer_update'
		return reverse(url, kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		if self.admin == 1 or self.detektyw == 1:
			self.is_staff = 1
		else:
			self.is_staff = 0
		super(CustomUser, self).save(*args, **kwargs)


class Pojazd(models.Model):
	numer_rejestracyjny = models.CharField(max_length=12)
	wlasciciel = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return self.numer_rejestracyjny