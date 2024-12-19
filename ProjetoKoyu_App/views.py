from django.shortcuts import render

from django.views.generic.edit import CreateView
from ProjetoKoyu_App import models

# Create your views here.
def AdicionarExercicioView(request):
    return render(request, 'ProjetoKoyu_App/adicionarExercicio-form.html', context={'message': 'Bem-vindo!'})
    
def AdicionarTreinoView(request):
    return render(request, 'ProjetoKoyu_App/adicionarTreino-form.html', context={'message': 'Bem-vindo!'})
    
def homepage(request):
    return render(request, 'ProjetoKoyu_App/index.html', context={'message': 'Bem-vindo!'})
