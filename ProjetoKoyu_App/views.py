from django.shortcuts import render

def adicionar_utilizador(request):
    return render(request, 'adicionar_utilizador.html')
