
from django import forms
 

from .models import Sprawa, Notatka
from uzytkownicy.models import CustomUser


from django.forms.models import inlineformset_factory




class SprawaCreateForm(forms.ModelForm):

	# detektyw = forms.Select(attrs={"name": "select_0","class": "form-control"})
	# detektyw = forms.ChoiceField(label='', choices=CustomUser.objects.filter(is_staff=True).order_by('nazwisko'))

	class Meta:
		model = Sprawa
		fields = ('nazwa', 'klient', 'typ_sprawy', 'detektyw', 'zawieszona', 'zamknieta', 'data_rozpoczecia', 'data_zakonczenia', 'dane_posiadane', 'opis_sprawy', 'zakres_czynnosci',)
		widgets = {'detektyw': forms.Select(attrs={'class':'form-control'}), 'klient': forms.Select(attrs={'class':'form-control'}), 'typ_sprawy': forms.Select(attrs={'class':'form-control'}),}
		# widgets = {'klient': forms.Select(attrs={'class':'form-control'}), }


	def __init__(self, *args, **kwargs):
		super(SprawaCreateForm, self).__init__(*args, **kwargs)
		
	# 	self.fields['detektyw'].widget = forms.Select(attrs={'class':'form-control'})
		self.fields['detektyw'].queryset = CustomUser.objects.filter(is_staff=True).order_by('nazwisko')
		self.fields['klient'].queryset = CustomUser.objects.filter(is_staff=False).order_by('nazwisko')






class SprawaCreateInlineForm(forms.ModelForm):



	class Meta:
		model = Sprawa
		fields = ('nazwa',)

	def __init__(self, *args, **kwargs):
		from django.forms.widgets import HiddenInput

		super(SprawaCreateInlineForm, self).__init__(*args, **kwargs)
		self.fields['nazwa'].widget = HiddenInput()






class NotatkaForm(forms.ModelForm):

	class Meta:
		model = Notatka
		fields = ['tresc', 'widoczna_dla_klienta',]
		widgets = {'tresc': forms.Textarea(attrs={'class': 'textarea form-control','placeholder': 'Treść', },)}
		labels = {
            'tresc': 'Treść notatki',
        }

	def __init__(self, *args, **kwargs):
		from django.forms.widgets import HiddenInput
		super(NotatkaForm, self).__init__(*args, **kwargs)

NotatkaFormset = inlineformset_factory(Sprawa, Notatka, form=NotatkaForm, extra=1, can_delete=True, can_delete_extra=True)





class BrudnopisUpdateForm(forms.ModelForm):

	# detektyw = forms.Select(attrs={"name": "select_0","class": "form-control"})
	# detektyw = forms.ChoiceField(label='', choices=CustomUser.objects.filter(is_staff=True).order_by('nazwisko'))

	class Meta:
		model = Sprawa
		fields = ('brudnopis',)
		# widgets = {'detektyw': forms.Select(attrs={'class':'form-control'}), 'klient': forms.Select(attrs={'class':'form-control'}), 'typ_sprawy': forms.Select(attrs={'class':'form-control'}),}
		# widgets = {'klient': forms.Select(attrs={'class':'form-control'}), }


	# def __init__(self, *args, **kwargs):
	# 	super(SprawaCreateForm, self).__init__(*args, **kwargs)
		
	# # 	self.fields['detektyw'].widget = forms.Select(attrs={'class':'form-control'})
	# 	self.fields['detektyw'].queryset = CustomUser.objects.filter(is_staff=True).order_by('nazwisko')
	# 	self.fields['klient'].queryset = CustomUser.objects.filter(is_staff=False).order_by('nazwisko')