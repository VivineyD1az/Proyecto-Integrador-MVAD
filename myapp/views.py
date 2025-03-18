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
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('data_entry')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

#Vista Ingresar datos
def enterdata(request):
    if request.method == 'POST':
        form = Consumeform(request.POST)
        if form.is_valid():
            form.save() #Guarda en la base de datos
    else:
        form = Consumeform()
    return render(request, 'data_entry.html', {'form': form})