from .models import *
from dataclasses import fields
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget
from django.forms import *
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Select, NumberInput, EmailInput, PasswordInput
from django import forms





class CategoriaForm(forms.ModelForm):
    class Meta:
            model = Categoria
            fields = '__all__'
            
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Categoria.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe una categoría con este nombre.')
        return nombre



class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Marca.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe una marca con este nombre.')
        return nombre
    

class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Presentacion.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe una presentación con este nombre.')
        return nombre


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if UnidadMedida.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe una unidad de medida con este nombre.')
        return nombre

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    marca = forms.ModelChoiceField(queryset=Marca.objects.all())
    presentacion = forms.ModelChoiceField(queryset=Presentacion.objects.all())
    unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all())
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all())
    class Meta:
        model = Producto
        fields = '__all__'
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Producto.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe un producto con este nombre.')
        return nombre


    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        self.fields['categoria'].queryset = Categoria.objects.filter(activado=True)
        self.fields['marca'].queryset = Marca.objects.filter(activado=True)
        self.fields['presentacion'].queryset = Presentacion.objects.filter(activado=True)
        self.fields['unidad_medida'].queryset = UnidadMedida.objects.filter(activado=True)
        self.fields['proveedor'].queryset = Proveedor.objects.filter(activado=True)
    
    

class ProveedorForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all())
    class Meta:
        model = Proveedor
        fields = '__all__'
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Proveedor.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError('Ya existe un proveedor con este nombre.')
        return nombre
    
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
    
        self.fields['marca'].queryset = Marca.objects.filter(activado=True)



class CompraForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.filter(activado=True))
    cantidad = forms.IntegerField(min_value=1)
    class Meta:
        model = compra
        fields = ['fechaingreso', 'valortotal', 'nombreproducto', 'cantidad', 'valorunitario']

class VentaForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.filter(activado=True))
    cantidad = forms.IntegerField(min_value=1)
    class Meta:
        model = venta
        fields = '__all__'

