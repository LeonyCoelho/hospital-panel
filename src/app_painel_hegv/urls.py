from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('painel/', views.painel, name='painel'),            # sem sala
    path('painel/<str:sala_nome>/', views.painel, name='painel_sala'),  # com sala
    path('leitos', views.leitos, name='leitos'),
    path('leitos/<str:sala_nome>/', views.leitos, name='leitos_sala'),  # com sala
    path('leito/<int:id>/editar/', views.editar_leito_page, name='editar_leito_page'),
    # path('leito/novo/', views.novo_leito, name='novo_leito'),
    path('api/create_leito/', views.create_leito),  # se você quiser manter esse endpoint


    path('api/get_leito/<int:id>/', views.get_leito, name='get_leito'),
    path('api/update_leito/<int:id>/', views.update_leito, name='update_leito'),
    path('get_all_leitos/<str:sala_nome>/', views.get_all_leitos, name='get_all_leitos'),
]