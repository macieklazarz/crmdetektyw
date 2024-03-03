from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField

from django import forms

from .models import CustomUser, Pojazd

from django.forms.models import inlineformset_factory



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Adres email', 'id': 'exampleInputEmail'}))
    imie = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Imię','id': 'exampleFirstName',}))
    nazwisko = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Nazwisko','id': 'exampleLastName',}))
    adres = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Adres','id': 'exampleInputAdres',}))
    numer_telefonu = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Numer telefonu','id': 'exampleInputTelefon',}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Hasło','id': 'exampleInputPassword1',}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Powtórz hasło','id': 'exampleInputPassword2',}))


    class Meta:
        model = CustomUser
        fields = ("email", "imie", "nazwisko", "adres", "numer_telefonu","password1", "password2")
        # widgets = {
        #     'email': EmailField(attrs={'class': 'form-control form-control-user', 'placeholder': 'Adres email', 'id': 'exampleInputEmail'}),
        # }



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class UserLoginForm(AuthenticationForm):


    # def __init__(self, *args, **kwargs):
    #     super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Adres email', 'id': 'exampleInputEmail'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Hasło',
            'id': 'exampleInputPassword',
        }
))




class CustomUserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Adres email', 'id': 'exampleInputEmail'}))
    imie = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Imię','id': 'exampleFirstName',}))
    nazwisko = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Nazwisko','id': 'exampleLastName',}))
    adres = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Adres','id': 'exampleInputEmail',}))
    numer_telefonu = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Numer telefonu','id': 'exampleInputEmail',}))
    inne = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-user','placeholder': 'Inne','id': 'exampleInputEmail',}))


    class Meta:
        model = CustomUser
        fields = ("email", "imie", "nazwisko", "adres", "numer_telefonu", "inne", "admin", "detektyw")

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        is_detektyw = kwargs.pop("is_detektyw", None)
        requestor_is_admin = kwargs.pop("requestor_is_admin", None)

        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        if not requestor_is_admin:
            self.fields['admin'].widget = HiddenInput()
            self.fields['detektyw'].widget = HiddenInput()
        if is_detektyw:
            self.fields['inne'].widget = HiddenInput()

class StaffUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Adres email', 'id': 'exampleInputEmail'}))
    imie = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Imię','id': 'exampleFirstName',}))
    nazwisko = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Nazwisko','id': 'exampleLastName',}))
    adres = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Adres','id': 'exampleInputEmail',}))
    numer_telefonu = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': 'Numer telefonu','id': 'exampleInputEmail',}))



    class Meta:
        model = CustomUser
        fields = ("email", "imie", "nazwisko", "adres", "numer_telefonu", "admin", "detektyw")

    # def __init__(self, *args, **kwargs):
    #     from django.forms.widgets import HiddenInput
    #     is_detektyw = kwargs.pop("is_detektyw", None)

    #     super(StaffUpdateForm, self).__init__(*args, **kwargs)
    #     if is_detektyw:
    #         self.fields['inne'].widget = HiddenInput()
class PojazdForm(forms.ModelForm):

    class Meta:
        model = Pojazd
        fields = ['numer_rejestracyjny',]
        widgets = {'numer_rejestracyjny' : forms.TextInput(
        attrs={'class': 'form-control form-control-user','placeholder': '','id': 'exampleInputEmail',})}

PojazdFormset = inlineformset_factory(CustomUser, Pojazd, form=PojazdForm, extra=3)