from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('painel/', views.painel, name='painel'),            # sem sala
    path('<str:sala_nome>/painel/', views.painel, name='painel_sala'),  # com sala
    path('<str:sala_nome>/leitos', views.leitos, name='leitos'),
    path('<str:sala_nome>/leitos/<str:sala_nome>/', views.leitos, name='leitos_sala'),  # com sala
    path('<str:sala_nome>/leito/<int:id>/editar/', views.editar_leito_page, name='editar_leito_page'),
    path('<str:sala_nome>/leito/novo/', views.novo_leito, name='novo_leito'),


    path('api/get_leito/<int:id>/', views.get_leito, name='get_leito'),
    path('api/update_leito/<int:id>/', views.update_leito, name='update_leito'),
    path('get_all_leitos/<str:sala_nome>/', views.get_all_leitos, name='get_all_leitos'),
]