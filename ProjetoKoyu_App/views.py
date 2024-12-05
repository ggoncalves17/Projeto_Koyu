from django.shortcuts import render

from django.views.generic.edit import CreateView
from ProjetoKoyu_App import models

# Create your views here.
class AdicionarExercicioView(CreateView):
    model = models.AdicionarExercicioModel
    fields = ['title', 'description']
    template_name = 'ProjetoKoyu_App/adicionarExercicio-form.html'
    
class AdicionarTreinoView(CreateView):
    model = models.AdicionarTreinoModel
    fields = ['title', 'description']
    template_name = 'ProjetoKoyu_App/adicionarTreino-form.html'
    
def homepage(request):
    return render(request, 'projeto_koyu/index.html', context={'message': 'Bem-vindo!'})
