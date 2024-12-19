from django.contrib import admin 
from django.urls import path, include

from ProjetoKoyu_App import views 

urlpatterns = [ 
    path('admin/', admin.site.urls),  
    path("", include('ProjetoKoyu_App.urls')),
]  