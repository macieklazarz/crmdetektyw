from django.db import models
from uzytkownicy.models import CustomUser
from django.utils import timezone
import uuid
# Create your models here.

class TypSprawy(models.Model):
	typ_sprawy = models.CharField(max_length = 20)


	def __str__(self):
		return self.typ_sprawy



class Sprawa(models.Model):
	id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable=False)
	nazwa = models.CharField(max_length = 50)
	klient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='klient')
	typ_sprawy = models.ForeignKey(TypSprawy, on_delete=models.SET_NULL, blank=True, null=True)
	detektyw = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
	zawieszona = models.BooleanField(default=False)
	zamknieta = models.BooleanField(default=False, verbose_name='Zamknięta')
	zgloszona_do_kpp = models.BooleanField(default=False , verbose_name='Zgłoszona do KPP')
	data_rozpoczecia = models.DateTimeField(default=timezone.now, verbose_name='Data rozpoczęcia')
	data_zakonczenia = models.DateTimeField(null=True,blank=True, verbose_name='Data zakończenia')
	dane_posiadane = models.TextField(max_length=1024, blank=True, null=True)
	opis_sprawy = models.TextField(max_length=1024, blank=True, null=True)
	zakres_czynnosci = models.TextField(max_length=1024, blank=True, null=True, verbose_name='Zakres czynności')
	brudnopis = models.TextField(max_length=1024, blank=True, null=True, verbose_name='Brudnopis')


	def get_notes(self):
		return Notatka.objects.filter(sprawa=self).order_by('-data_utworzenia')


	def get_absolute_url(self):

		return reverse('sprawy: case_detail', kwargs={'pk': self.pk})


	def __str__(self):
		return self.nazwa


class Notatka(models.Model):
	autor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
	sprawa = models.ForeignKey(Sprawa, on_delete=models.CASCADE)
	tresc = models.TextField(max_length=1024, blank=True, null=True)
	data_utworzenia = models.DateTimeField(default=timezone.now)
	widoczna_dla_klienta = models.BooleanField(default=True)