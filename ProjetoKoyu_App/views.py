
from django.shortcuts import render, redirect
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

        print(utilizador)

        if utilizador is not None and utilizador.ut_tipo == "Gestor":

            login(request, utilizador)
            messages.success(request, "Credenciais Corretas.")
            return redirect("/")
        else:
            messages.error(request, "Credenciais Incorretas.")

    return render(request, "projeto_koyu/login.html")

def dashboard(request):
    return render(request, 'projeto_koyu/dashboard.html')

def listar_utilizadores(request):
    return render(request, 'projeto_koyu/listar_utilizadores.html')

# View de adicionar utilizador
def adicionar_utilizador_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')
        tipo_utilizador = request.POST.get('tipo_utilizador') 
        if tipo_utilizador == "Utilizador":
            nif=request.POST.get('nif')
        else:
            nif=0

        # Verifica se o utilizador já existe
        if Utilizador.objects.filter(ut_mail=email).exists():
            messages.error(request, "Utilizador já existe!")
        elif nif and not nif.isdigit():
            messages.error(request, "NIF deve conter apenas números.")
        else:
            user = Utilizador.objects.create_user(
                email=email, 
                password="teste", 
                ut_nome=nome, 
                ut_telefone=contacto, 
                ut_nif=nif,
                ut_tipo=tipo_utilizador, 
                ut_estado=1,
                ut_foto="nada"
            )
            messages.success(request, "Utilizador adicionado com sucesso!")
            return redirect("/") 

    return render(request, 'projeto_koyu/adicionar_utilizador.html')


# View de editar utilizador
def editar_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id) 

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')
        nif = request.POST.get('nif')

        # Atualiza os dados do utilizador
        user.username = nome
        user.email = email
        user.contacto = contacto  
        user.nif = nif 
        try:
            user.save()
            messages.success(request, "Utilizador atualizado com sucesso!")
            return redirect('homepage')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar utilizador: {str(e)}")

    return render(request, 'projeto_koyu/editar_utilizador.html', {'user': user})

# View de detalhes utilizador
def detalhes_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id)

    if request.method == 'POST':
        if 'editar' in request.POST:
            messages.info(request, f"Editar utilizador: {user.username}")
            return redirect('editar_utilizador', id=user.id)
        elif 'desativar' in request.POST:
            user.is_active = False
            user.save()
            messages.success(request, f"Utilizador {user.username} foi desativado.")
            return redirect('homepage')

    return render(request, 'projeto_koyu/detalhes_utilizador.html', {'user': user})
