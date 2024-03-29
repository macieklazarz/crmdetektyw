from django.contrib import admin
from sprawy.models import Sprawa, TypSprawy, Notatka
# Register your models here.

@admin.register(Sprawa)
class SprawyAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'klient', 'typ_sprawy', 'detektyw', 'zawieszona', 'zamknieta', 'zgloszona_do_kpp', 'data_rozpoczecia', 'data_zakonczenia')
	search_fields = ('nazwa',)


@admin.register(TypSprawy)
class TypSprawyAdmin(admin.ModelAdmin):
	list_display = ('typ_sprawy',)
	search_fields = ('typ_sprawy',)


@admin.register(Notatka)
class NotatkaAdmin(admin.ModelAdmin):
	list_display = ('sprawa', 'autor', 'tresc')
	search_fields = ('sprawa', 'autor', 'tresc')