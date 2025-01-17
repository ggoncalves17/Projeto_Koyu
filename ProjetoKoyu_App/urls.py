from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('adicionarExercicio/', views.AdicionarExercicioView, name='Adicionar-Exercicio'),
    path('editarExercicio/', views.EditarExercicioView, name='Editar-Exercicio'),
    path('detalhesExercicio/', views.DetalhesExercicioView, name='Detalhes-Exercicio'),
    path('adicionarTreino/', views.AdicionarTreinoView, name='Adicionar-Treino'),
    path('editarTreino/', views.EditarTreinoView, name='Editar-Treino'),
    path('detalhesTreino/', views.DetalhesTreinoView, name='Detalhes-Treino'),
]