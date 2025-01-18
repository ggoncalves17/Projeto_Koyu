from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

<<<<<<< HEAD
urlpatterns = [    
=======
urlpatterns = [
    path('', views.homepage, name='homepage'),
>>>>>>> fd60aebf4e593914e81b6293695a82a8fed8a55d
    path('login/', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('listar_utilizadores', views.listar_utilizadores, name='listar_utilizadores'),
    path('adicionar_utilizador/', views.adicionar_utilizador_view, name='adicionar_utilizador'),
    path('editar_utilizador/<int:id>/', views.editar_utilizador_view, name='editar_utilizador'),
    path('detalhes_utilizador/<int:id>/', views.detalhes_utilizador_view, name='detalhes_utilizador'),
    path('apagar_utilizador/<int:ut_id>/', views.apagar_utilizador, name='apagar_utilizador'),
<<<<<<< HEAD
    path('logout/', views.logout_view, name='logout'),
=======
    path('listar_treinos/', views.listar_treinos, name='listar_treinos'),    
    path('eliminar_treino/<int:treino_id>/', views.eliminar_treino, name='eliminar_treino')
>>>>>>> fd60aebf4e593914e81b6293695a82a8fed8a55d
]
