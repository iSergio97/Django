#encoding:utf-8
from django import forms
   
class IdiomaBusquedaForm(forms.Form):
    idioma = forms.CharField(label="Idioma", widget=forms.TextInput, required=True)
    
class EventoBusquedaYearForm(forms.Form):
    year = forms.IntegerField(label="Año del evento", widget=forms.TextInput, required=True)