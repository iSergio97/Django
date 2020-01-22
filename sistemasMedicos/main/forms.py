from django import forms

class UserRegisterForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    contraseña = forms.CharField()


class UserLogin(forms.Form):
    username = forms.CharField()
    contraseña = forms.CharField()
