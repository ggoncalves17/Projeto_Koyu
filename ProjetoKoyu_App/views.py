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
    return render(request, 'projeto_koyu/login.html')

def dashboard(request):
    return render(request, 'projeto_koyu/dashboard.html')

def listar_utilizadores(request):
    return render(request, 'projeto_koyu/listar_utilizadores.html')
