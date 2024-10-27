
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms import *
from app.models import *
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
import re




class AdministradorForm(forms.ModelForm):
    username = forms.CharField(
        label="Nombre",
        max_length=150,
    )
    email = forms.EmailField(
        label="Correo electrónico",
        max_length=150,
        widget=forms.EmailInput(attrs={"placeholder": ""})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": "password-input"}),
        required=True, 
        validators=[MinLengthValidator(8, _("La contraseña debe tener al menos 8 caracteres."))]
    )
    conf_password = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": "password-input"}),
        required=True
    )
    numero_documento = forms.IntegerField(
        label="Número de documento",
        validators=[MaxValueValidator(9999999999, _("El número de documento debe tener entre 8 y 10 dígitos."))]
    )
    telefono = forms.IntegerField(
        label="Teléfono",
        validators=[MaxValueValidator(9999999999, _("El teléfono debe tener entre 7 y 10 dígitos."))]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
        self.fields["username"].widget.attrs["autofocus"] = True

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.search(r'\d', username):
            raise forms.ValidationError(_("El nombre no puede contener números."))
        return username

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")

       
        if User.objects.filter(username=self.cleaned_data.get('username')).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            raise forms.ValidationError(_("Este nombre de usuario ya está en uso."))

      
        if User.objects.filter(email=email).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            raise forms.ValidationError(_("Este correo electrónico ya está en uso."))

       
        if password1 != password2:
            self.add_error("conf_password", _("Las contraseñas no coinciden."))

        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if self.instance.pk:
            user = self.instance.user
            if username and user.username != username:
                user.username = username
            if email and user.email != email:
                user.email = email
            if password:
                user.set_password(password)
            user.save()
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

        administrador = super().save(commit=False)
        administrador.user = user
        if commit:
            administrador.save()
        return administrador

    class Meta:
        model = Administrador
        fields = ["username", "email", "tipo_documento", "numero_documento", "telefono", "password", "conf_password"]
        widgets = {
            "tipo_documento": forms.Select(attrs={"placeholder": ""}),
            "numero_documento": forms.NumberInput(attrs={"min": 10000000, "max": 9999999999, "placeholder": ""}),
            "telefono": forms.NumberInput(attrs={"min": 1000000, "max": 9999999999, "placeholder": ""}),
            "password": forms.PasswordInput(attrs={"placeholder": ""}),
            "conf_password": forms.PasswordInput(attrs={"placeholder": ""})
        }

# -----------------------------------------------------------------------------------------------
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput, Select, NumberInput
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": ""})
    )
    email = forms.EmailField(
        label="Email",
        max_length=150,
        widget=forms.EmailInput(attrs={"placeholder": ""})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": ""}),
        required=True
    )
    conf_password = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": ""}),
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")
        telefono = cleaned_data.get("telefono")

        # Validar que el nombre de usuario no contenga números
        if any(char.isdigit() for char in username):
            self.add_error('username', "El nombre de usuario no puede contener números.")

        # Validar que el nombre de usuario no esté en uso
        if User.objects.filter(username=username).exclude(pk=self.instance.user.pk if self.instance and hasattr(self.instance, 'user') else None).exists():
            self.add_error('username', "Este nombre de usuario ya está en uso.")
        
        # Validar que el correo no esté en uso
        if User.objects.filter(email=email).exclude(pk=self.instance.user.pk if self.instance and hasattr(self.instance, 'user') else None).exists():
            self.add_error('email', "Este correo electrónico ya está en uso.")
        
        # Validar que las contraseñas coincidan
        if password1 != password2:
            self.add_error('conf_password', "Las contraseñas no coinciden.")

        # Validar que el número de teléfono tenga 10 dígitos
        if len(telefono) != 10:
            self.add_error('telefono', "El número de teléfono debe tener exactamente 10 dígitos.")

        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if self.instance.pk and hasattr(self.instance, 'user'):
            user = self.instance.user
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  
            )
            self.instance.user = user 

        empleado = super().save(commit=False)
        empleado.contrasena = password
        empleado.conf_contrasena = cleaned_data.get('conf_password')
        if commit:
            empleado.save()
        return empleado

    class Meta:
        model = Empleado
        fields = ["username", "email", "tipo_documento", "numero_documento", "telefono", "password", "conf_password"]
        widgets = {
            "tipo_documento": forms.Select(attrs={"placeholder": "Tipo de documento"}),
            "numero_documento": forms.TextInput(attrs={"placeholder": "Número de documento"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Teléfono"}),
        }