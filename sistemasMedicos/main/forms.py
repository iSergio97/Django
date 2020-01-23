from django import forms


class UserLogin(forms.Form):
    username = forms.CharField()
    contraseña = forms.CharField()


class buscarTemasTitulo(forms.Form):
    titulo = forms.CharField(label="Palabra clave", widget=forms.TextInput, required=True)
