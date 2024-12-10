from django.shortcuts import render

def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

def dashboard(request):
    return render(request, 'projeto_koyu/dashboard.html')

def listar_utilizadores(request):
    return render(request, 'projeto_koyu/listar_utilizadores.html')
