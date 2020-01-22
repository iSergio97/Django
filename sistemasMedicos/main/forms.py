from django import forms


class UserLogin(forms.Form):
    username = forms.CharField()
    contraseña = forms.CharField()


class buscarNoticiasCabecera(forms.Form):
    temas = forms.CharField(label="Palabra clave", widget=forms.TextInput, required=True)


class buscarArticulosCabecera(forms.Form):
    temas = forms.CharField(label="Palabra clave", widget=forms.TextInput, required=True)
