from django import forms


class UserLogin(forms.Form):
    username = forms.CharField()
    contraseña = forms.CharField()


class buscarNoticiasCabecera(forms.Form):
    cabecera = forms.CharField()


class buscarArticulosCabecera(forms.Form):
    cabecera = forms.CharField()
