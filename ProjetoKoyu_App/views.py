from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

# Página inicial
def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

# View de login
def login_view(request):
    '''if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirecionar para a página inicial
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')'''
    return render(request, 'projeto_koyu/login.html')


