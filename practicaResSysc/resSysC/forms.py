# encoding:utf-8
from django import forms

class IdAnimeFormulario(forms.Form):
    genero = forms.CharField(label="Género", widget=forms.TextInput, required=True)