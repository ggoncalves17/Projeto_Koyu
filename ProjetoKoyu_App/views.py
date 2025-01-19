from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from .models import Equipamento, Exercicios, Historico, PlanoTreinos, Utilizador, UtilizadorManager, Modalidade, Categoria
from .forms import UtilizadorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

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

#Funcoes relativas à pagina detalhes utilizador
@login_required
def detalhes_perfil(request):
    user = request.user
    
    if request.method == "POST":

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        foto = request.FILES.get('fotoPerfil')

        if foto is None:
            nome_foto = user.ut_foto
            print(user.ut_foto)

        # Validações básicas (opcional)
        if not nome or not email:
            messages.error(request, "Nome e Email são obrigatórios.")
            return render(request, 'projeto_koyu/detalhes_perfil.html', {'user': user})
        
        if foto is None:
            nome_foto = user.ut_foto
        else:
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')

            pasta = "ProjetoKoyu_App\static\images\listar_utilizadores\ProfilePhotos"

            nome_foto = f"{nome}_{timestamp}_{foto.name}"

            fs = FileSystemStorage(location=pasta)
            fs.save(nome_foto, foto)
            
        # Atualiza os dados do utilizador
        user.ut_nome = nome
        user.ut_mail = email
        user.ut_telefone = telefone 
        user.ut_foto = nome_foto
        user.save()
        messages.success(request, "Dados atualizados com sucesso!")
        return redirect('detalhes_perfil')
        
    return render(request, 'projeto_koyu/detalhes_perfil.html', {'user': user})

@login_required
def apagar_conta(request, ut_id):
    utilizador = get_object_or_404(Utilizador, id=ut_id)
    utilizador.ut_estado = 0
    utilizador.save()
    messages.success(request, "Conta apagada com sucesso.")
    return redirect('login')

#Funcoes alterar password
@login_required
def alterar_password(request, user_id):
    user = get_object_or_404(Utilizador, id=user_id)  # Substitua Utilizador pelo nome correto do modelo

    if request.method == "POST":
        # Obter os dados do formulário
        password_atual = request.POST.get('password_atual')
        nova_password = request.POST.get('nova_password')
        confirma_password = request.POST.get('confirma_password')

        # Verificar se a password atual está correta
        if not check_password(password_atual, user.password):
            messages.error(request, "A password atual está incorreta.")
            return render(request, 'projeto_koyu/detalhes_perfil.html', {'user': user, 'popup_password_open': True})

        # Verificar se a password senha e a confirmação coincidem
        if nova_password != confirma_password:
            messages.error(request, "A nova password e a confirmação não coincidem.")
            return render(request, 'projeto_koyu/detalhes_perfil.html', {'user': user, 'popup_password_open': True})

        # Atualizar a password na base de dados (encriptada)
        user.password = make_password(nova_password, hasher='default')  
        user.save()

        messages.success(request, "Password alterada com sucesso!")
        return redirect('detalhes_perfil')

    return redirect('detalhes_perfil')



#Funcoes relativas a pagina listar utilizadores
@login_required
def listar_utilizadores(request):
    utilizadores = Utilizador.objects.all()
    return render(request, 'projeto_koyu/listar_utilizadores.html', {'utilizadores':utilizadores})

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

        foto = request.FILES.get('fotoPerfil')

        # Verifica se o utilizador já existe
        if Utilizador.objects.filter(ut_mail=email).exists():
            messages.error(request, "Utilizador já existe!")
        elif nif and not nif.isdigit():
            messages.error(request, "NIF deve conter apenas números.")
        else:
            if foto is None:
                nome_foto = "profile_picture.jpeg"
            else:
                pasta = "ProjetoKoyu_App\static\images\listar_utilizadores\ProfilePhotos"
                if not os.path.exists(pasta):
                    os.makedirs(pasta)

                timestamp = timezone.now().strftime('%Y%m%d%H%M%S')

                nome_foto = f"{nome}_{timestamp}_{foto.name}"

                fs = FileSystemStorage(location=pasta)
                fs.save(nome_foto, foto)

            user = Utilizador.objects.create_user(
                email=email, 
                password="teste", 
                ut_nome=nome, 
                ut_telefone=contacto, 
                ut_nif=nif,
                ut_tipo=tipo_utilizador, 
                ut_estado=1,
                ut_foto=nome_foto
            )
            return redirect("/listar_utilizadores")

    return render(request, 'projeto_koyu/adicionar_utilizador.html')

# View de detalhes utilizador
@login_required
def detalhes_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id)

    if request.method == 'POST':
        # Verifica a ação enviada
        if request.POST.get('acao') == 'alternar_estado':
            user.ut_estado = 2 if user.ut_estado == 1 else 1  # Alterna entre 2 (Inativo) e 1 (Ativo)
            user.save()
            estado = "desativado" if user.ut_estado == 2 else "ativado"
            messages.success(request, f"O estado do utilizador {user.ut_nome} foi {estado} com sucesso!")
            return redirect('detalhes_utilizador', id=user.id)

    return render(request, 'projeto_koyu/detalhes_utilizador.html', {'user': user})

@login_required
def editar_utilizador_view(request, id):
    user = get_object_or_404(Utilizador, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')
        tipo_utilizador = request.POST.get('tipo_utilizador')  
        foto = request.FILES.get('fotoPerfil')

        if tipo_utilizador == "Utilizador":
            nif = request.POST.get('nif')

            # Valida o NIF
            if not nif.isdigit() or len(nif) != 9:
                messages.error(request, "O NIF deve conter exatamente 9 dígitos.")
                return render(request, 'projeto_koyu/editar_utilizador.html', {"user": user})
        else:
            nif = 0  
        
        nif = int(nif) if nif and nif != "0" else 0

        if foto is None:
            nome_foto = user.ut_foto
        else:
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')

            pasta = "ProjetoKoyu_App\static\images\listar_utilizadores\ProfilePhotos"

            nome_foto = f"{nome}_{timestamp}_{foto.name}"

            fs = FileSystemStorage(location=pasta)
            fs.save(nome_foto, foto)
        
        # Atualiza os campos do utilizador
        user.ut_nome = nome
        user.ut_mail = email
        user.ut_telefone = contacto
        user.ut_nif = nif
        user.ut_tipo = tipo_utilizador
        user.ut_foto = nome_foto
        user.save()
        messages.success(request, "Utilizador atualizado com sucesso!")
        return redirect("/listar_utilizadores")  
    return render(request, 'projeto_koyu/editar_utilizador.html', {"user": user})
  
@login_required
def apagar_utilizador(request, ut_id):
    utilizador = get_object_or_404(Utilizador, id=ut_id)
    utilizador.ut_estado = 0
    utilizador.save()
    return redirect('listar_utilizadores')
  
#Funcoes relativas a pagina listar treinos
def listar_treinos(request):
    treinos = PlanoTreinos.objects.prefetch_related('modalidade').all().order_by('id')  # Obtém todos os treinos
    modalidades = Modalidade.objects.all()
    categorias = Categoria.objects.prefetch_related('categoria_planostreino').all()
    return render(request, 'projeto_koyu/listar_treinos.html', {'treinos': treinos, 'modalidades':modalidades, 'categorias':categorias})
  
@login_required
def eliminar_treino(request, treino_id):
    treino = get_object_or_404(PlanoTreinos, id=treino_id)
    if request.method == 'POST':
        treino.delete()
        return redirect('listar_treinos')
    return redirect('listar_treinos')

#Listar exercicios
@login_required
def listar_exercicios(request):
    exercicios = Exercicios.objects.select_related('equipamento').all()
    return render(request, 'projeto_koyu/listar_exercicios.html', {'exercicios': exercicios})

@login_required
def apagar_exercicio(request, exercicio_id):
    exercicio = get_object_or_404(Exercicios, id=exercicio_id)
    exercicio.delete()
    return redirect('listar_exercicios')

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")
