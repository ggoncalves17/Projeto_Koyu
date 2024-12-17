from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Utilizador
from .forms import UtilizadorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
import time

def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

def login(request):

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