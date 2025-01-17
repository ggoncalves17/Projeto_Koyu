from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('listar_utilizadores', views.listar_utilizadores, name='listar_utilizadores'),
    path('apagar_utilizador/<int:ut_id>/', views.apagar_utilizador, name='apagar_utilizador')
]


