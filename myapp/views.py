from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import Consumeform, CustomUserForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def signupview(request):
    print("Vista signupview llamada")  

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            print("Formulario válido. Guardando el usuario...")
            user = form.save()
            messages.success(request, 'Usuario registrado correctamente')
            login(request, user)
            return redirect('data_entry')
        else:
            print("Formulario no válido.")
            print(form.errors)  
            messages.error(request, 'Hubo un error con el registro. Intenta nuevamente.')
    else:
        form = CustomUserForm()

    return render(request, 'register.html', {'form': form})

#Vista Login
class loginview(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

    def get_form(self, form_class=None):
        """
        Obtiene el formulario de autenticación.
        """
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        """
        Lógica cuando el formulario es válido: autentica y verifica el usuario.
        """
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )
        
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username or password")
            return self.form_invalid(form)

    def form_invalid(self, form):
        """
        Maneja el caso de un formulario inválido.
        """
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)

    def get_success_url(self):
        """
        URL de redirección después de un inicio de sesión exitoso.
        """
        return reverse_lazy('data_entry')

#Vista Ingresar datos
def enterdata(request):
    print("Vista enterdata llamada")
    
    if request.method == 'POST':
        form = Consumeform(request.POST)
        if form.is_valid():
            form.save() #Guarda en la base de datos
    else:
        form = Consumeform()
    return render(request, 'data_entry.html', {'form': form})

#Vista de Inicio
def home(request):
    return render(request, 'home.html')