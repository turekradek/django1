from django.forms import ModelForm
from .models import Zawodnik, Ocena
from django import forms
class ZawodnikForm( ModelForm ):
    class Meta:
        model = Zawodnik
        fields = ['nazwisko', 'imie','pas', 'belki','email','wiek','poczatek']

class UploadFileForm( forms.Form ):
    # title = forms.CharField( max_length=50 )
    file = forms.FileField()

class TrescPlikuFrom(forms.Form):
    tytul = forms.CharField( max_length=50 )
    plik = forms.FileField()

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['uzasadnienie','ranking']

