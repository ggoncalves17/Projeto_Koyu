from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adicionarExercicio/', views.AdicionarExercicioView, name='Adicionar-Exercicio'),
    path('adicionarTreino/', views.AdicionarTreinoView, name='Adicionar-Treino'),
]

