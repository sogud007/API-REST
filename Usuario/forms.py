# Usuario/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuarios

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuarios
        fields = ('NOMBRE', 'CORREO')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuarios
        fields = UserChangeForm.Meta.fields