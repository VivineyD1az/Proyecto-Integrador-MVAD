from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        }
    #password = forms.CharField(widget=forms.PasswordInput())
    
    #class Meta:
     #   model = CustomUser
      #  fields = ['first_name', 'last_name', 'username', 'password']
    
    def save(self, commit = True):
       user = super().save(commit = False)
       if commit:
           user.save()
       return user   
    
#Formulario de Login
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Nombre de usuario",
            }
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Contraseña"}
        )