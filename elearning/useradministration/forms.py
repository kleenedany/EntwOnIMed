from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Benutzername')