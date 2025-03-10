from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Consume, CustomUser

#Formulario de Ingreso de datos
class Consumeform(forms.ModelForm):
    class Meta:
        model = Consume
        fields = ['month', 'total_cost']
        widgets = {
            'month': forms.NumberInput(attrs={'placeholder': 'N° de mes'}),
            'total_cost': forms.NumberInput(attrs={'placeholder': 'Costo total del consumo'})
        }

#Formulario de Registro
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password']