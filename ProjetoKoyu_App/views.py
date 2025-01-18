from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Equipamento, Exercicios, Historico, PlanoTreinos, Utilizador, UtilizadorManager
from .forms import UtilizadorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import HttpResponse

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
    #Menu
    if request.method == "POST":
        exercicios = request.POST.get("exercicios")
        treinos = request.POST.get("treinos")
        utilizadores = request.POST.get("utilizadores")
        perfil = request.POST.get("perfil")
        
        if utilizadores: 
            return redirect("/listar_utilizadores")

    #Estatisticas
    utilizadores = Utilizador.objects.all()
    n_utilizadores = len(utilizadores)
    exercicios = Exercicios.objects.all()
    n_exercicios = len(exercicios)
    treinosrealizados = Historico.objects.all()
    n_treinosrealizados = len(treinosrealizados)

    #Historico
    ultimos_treinos = PlanoTreinos.objects.order_by('-id')[:5]
    ultimos_exercicios = Exercicios.objects.order_by('-id')[:5]
    ultimos_users = Utilizador.objects.order_by('-id')[:5]
    ultimos_equipamentos = Equipamento.objects.order_by('-id')[:5]

    return render(request, 'projeto_koyu/dashboard.html',{'n_utilizadores':n_utilizadores,'n_exercicios':n_exercicios,'n_treinosrealizados':n_treinosrealizados,
                                                          'ultimos_treinos':ultimos_treinos,'ultimos_exercicios':ultimos_exercicios,
                                                          'ultimos_users':ultimos_users,'ultimos_equipamentos':ultimos_equipamentos})

#Funcoes relativas a pagina listar utilizadores
@login_required
def listar_utilizadores(request):
    utilizadores = Utilizador.objects.all()
    return render(request, 'projeto_koyu/listar_utilizadores.html', {'utilizadores':utilizadores})

# View de adicionar utilizador
@login_required
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
  
@login_required
def apagar_utilizador(request, ut_id):
    utilizador = get_object_or_404(Utilizador, id=ut_id)
    utilizador.ut_estado = 0
    utilizador.save()
    return redirect('listar_utilizadores')

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")
