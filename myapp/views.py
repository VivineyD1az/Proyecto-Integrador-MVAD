from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import Consumeform, CustomUserForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

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
        else:
            print(form.errors)
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