from django import forms
from django.forms import Form
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class AuthForm(Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email'}), validators=[validators.EmailValidator], label=_('Адрес электронной почты'))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label=_('Пароль'))
