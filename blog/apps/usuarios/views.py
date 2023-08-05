from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirección a la página de home post login
        else:
            messages.error(request, 'Usuario o contraseña invalido, intente de nuevo.')
    return render(request, 'usuarios/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirección a la página de login post logout

class Registro(CreateView):
    #FORMULARIO DJANGO
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'