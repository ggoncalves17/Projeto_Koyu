from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

# View de adicionar utilizador
def adicionar_utilizador_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        contacto = request.POST.get('contacto')
        nif = request.POST.get('nif', None)

        # Verifica se o utilizador já existe
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Utilizador já existe!")
        elif nif and not nif.isdigit():
            messages.error(request, "NIF deve conter apenas números.")
        else:
            # Criação do utilizador
            user = User.objects.create_user(username=nome, email=email)
            user.save()
            messages.success(request, "Utilizador adicionado com sucesso!")
            return redirect('homepage') 

    return render(request, 'projeto_koyu/adicionar_utilizador.html')

# View de editar utilizador
def editar_utilizador_view(request, id):
    user = get_object_or_404(User, id=id) 

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
    user = get_object_or_404(User, id=id)

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