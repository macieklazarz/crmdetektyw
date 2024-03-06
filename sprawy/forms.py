
from django import forms
 

from .models import Sprawa
from uzytkownicy.models import CustomUser




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



