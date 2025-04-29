from django.urls import path
from . import views

urlpatterns = [
    path('painel/', views.painel, name='painel'),            # sem sala
    path('painel/<str:sala_nome>/', views.painel, name='painel_sala'),  # com sala
    path('leitos', views.leitos, name='leitos'),
    path('get_all_leitos/<str:sala_nome>/', views.get_all_leitos, name='get_all_leitos'),
]