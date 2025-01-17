from django.shortcuts import render

from django.views.generic.edit import CreateView
from ProjetoKoyu_App import models

# Create your views here.
def AdicionarExercicioView(request):
    return render(request, 'projeto_koyu/adicionarExercicio-form.html', context={'message': 'Bem-vindo!'})
    
def EditarExercicioView(request):
    return render(request, 'projeto_koyu/editarExercicio-form.html', context={'message': 'Bem-vindo!'})
    
def DetalhesExercicioView(request):
    return render(request, 'projeto_koyu/detalhesExercicio-form.html', context={'message': 'Bem-vindo!'})
    
def AdicionarTreinoView(request):
    return render(request, 'projeto_koyu/adicionarTreino-form.html', context={'message': 'Bem-vindo!'})
     
def EditarTreinoView(request):
    return render(request, 'projeto_koyu/editarTreino-form.html', context={'message': 'Bem-vindo!'})

def DetalhesTreinoView(request):
    return render(request, 'projeto_koyu/detalhesTreino-form.html', context={'message': 'Bem-vindo!'})