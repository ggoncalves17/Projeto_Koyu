from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Utilizador
from .forms import UtilizadorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

# Página inicial
def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

# View de login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        lista_utilizadores = Utilizador.objects.filter(ut_mail=email)

        if lista_utilizadores:
            for utilizador in lista_utilizadores:
                if utilizador.ut_pass == password: 
                    messages.success(request, "Credenciais Corretas.")
                    return redirect("/")
            messages.error(request, "Credenciais Incorretas.")
        else:
            messages.error(request, "Utilizador não encontrado.")

    return render(request, "projeto_koyu/login.html")

def dashboard(request):
    return render(request, 'projeto_koyu/dashboard.html')

def listar_utilizadores(request):
    return render(request, 'projeto_koyu/listar_utilizadores.html')
