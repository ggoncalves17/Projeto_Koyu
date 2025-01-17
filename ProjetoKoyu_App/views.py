from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Utilizador, UtilizadorManager
from .forms import UtilizadorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Página inicial
@login_required
def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

# View de login
def login_view(request):

    # utilizadorTeste = Utilizador.objects.create_user(
    #      email="teste@gmail.com", 
    #      password="teste", 
    #      ut_nome="Teste",
    #      ut_estado=1,
    #      ut_telefone=910234567,
    #      ut_foto="Teste",
    #      ut_tipo="Gestor",
    #      ut_nif=210234567,
    #      )
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        utilizador = authenticate(request, ut_mail=email, password=password)

        if utilizador is not None and utilizador.ut_estado == 1:
            # Caso o utilizador seja Gestor vai para dashboard
            if utilizador.ut_tipo == "Gestor":
                login(request, utilizador)
                return redirect("/dashboard")
            # Caso o utilizador seja utilizador comum, fica na mesma página pois apenas foi desenvolvido a parte do gestor
            else:
                messages.error(request, "Credenciais Corretas (Páginas Utilizador em Desenvolvimento)")
        else:
            messages.error(request, "Credenciais Incorretas.")

    return render(request, "projeto_koyu/login.html")

@login_required
def dashboard(request):
    return render(request, 'projeto_koyu/dashboard.html')

#Funcoes relativas a pagina listar utilizadores
@login_required
def listar_utilizadores(request):
    utilizadores = Utilizador.objects.all()
    return render(request, 'projeto_koyu/listar_utilizadores.html', {'utilizadores':utilizadores})
  
@login_required
def apagar_utilizador(request, ut_id):
    utilizador = get_object_or_404(Utilizador, id=ut_id)
    utilizador.ut_estado = 0
    utilizador.save()
    return redirect('listar_utilizadores')
