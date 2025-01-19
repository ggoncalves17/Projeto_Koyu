from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    
    path('login/', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('detalhes_perfil', views.detalhes_perfil, name='detalhes_perfil'),
    path('apagar_conta/<int:ut_id>/', views.apagar_conta, name='apagar_conta'),
    path('alterar_password/<int:user_id>/', views.alterar_password, name='alterar_password'),
    path('listar_utilizadores', views.listar_utilizadores, name='listar_utilizadores'),
    path('adicionar_utilizador/', views.adicionar_utilizador_view, name='adicionar_utilizador'),
    path('editar_utilizador/<int:id>/', views.editar_utilizador_view, name='editar_utilizador'),
    path('detalhes_utilizador/<int:id>/', views.detalhes_utilizador_view, name='detalhes_utilizador'),
    path('apagar_utilizador/<int:ut_id>/', views.apagar_utilizador, name='apagar_utilizador'),
    path('listar_exercicios', views.listar_exercicios, name='listar_exercicios'),
    path('apagar_exercicio/<int:exercicio_id>/', views.apagar_exercicio, name='apagar_exercicio'),
    path('logout/', views.logout_view, name='logout'),
    path('listar_treinos/', views.listar_treinos, name='listar_treinos'),    
    path('eliminar_treino/<int:treino_id>/', views.eliminar_treino, name='eliminar_treino')
]
