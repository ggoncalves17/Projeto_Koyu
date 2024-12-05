from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_utilizador, name='adicionar_utilizador'),
]
