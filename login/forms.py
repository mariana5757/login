from django import forms

class CreateUser(forms.Form):
    name = forms.CharField(label='Nombre')
    user = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    confirm_password = forms.CharField(label='Confirm Password')

class Login(forms.Form):
    user = forms.CharField(label='Username')
    password = forms.CharField(label='Password')