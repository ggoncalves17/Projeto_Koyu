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

@login_required
def editar_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')
        tipo_utilizador = request.POST.get('tipo_utilizador')  
        if tipo_utilizador == "Utilizador":
            nif = request.POST.get('nif')

            # Valida o NIF
            if not nif.isdigit() or len(nif) != 9:
                messages.error(request, "O NIF deve conter exatamente 9 dígitos.")
                return render(request, 'projeto_koyu/editar_utilizador.html', {"user": user})
        else:
            nif = 0  
        
        nif = int(nif) if nif and nif != "0" else 0
        
        # Atualiza os campos do utilizador
        user.ut_nome = nome
        user.ut_mail = email
        user.ut_telefone = contacto
        user.ut_nif = nif
        user.ut_tipo = tipo_utilizador
        user.ut_foto = "nada"
        user.save()
        messages.success(request, "Utilizador atualizado com sucesso!")
        return redirect("/")  # Redireciona para a página inicial ou outra página desejada

    # Renderiza o formulário com os dados do utilizador
    return render(request, 'projeto_koyu/editar_utilizador.html', {"user": user})


# View de detalhes utilizador
@login_required
def detalhes_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id)

    if request.method == 'POST':
        # Verifica a ação enviada
        if request.POST.get('acao') == 'alternar_estado':
            user.ut_estado = 0 if user.ut_estado == 1 else 1  # Alterna entre 0 e 1
            user.save()
            estado = "desativado" if user.ut_estado == 0 else "ativado"
            messages.success(request, f"O estado do utilizador {user.ut_nome} foi {estado} com sucesso!")
            return redirect('detalhes_utilizador', id=user.id)

    return render(request, 'projeto_koyu/detalhes_utilizador.html', {'user': user})