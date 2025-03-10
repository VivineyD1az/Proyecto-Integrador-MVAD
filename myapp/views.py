from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import Consumeform, CustomUserForm

# Create your views here.

#Vista Register
class signupview(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login.html')
        
        return render(request, 'register.html', {'form': form})

#Vista Login
class loginview(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('data_entry.html')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

#Vista Ingresar datos
def enterdata(request):
    if request.method == 'POST':
        form = Consumeform(request.POST)
        if form.is_valid():
            form.save() #Guarda en la base de datos
    else:
        form = Consumeform()
    return render(request, 'data_entry.html', {'form': form})