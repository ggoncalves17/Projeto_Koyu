from django.shortcuts import render

def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})

def adicionar_utilizador(request):
    return render(request, 'projeto_koyu/adicionar_utilizador.html')


