from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),
    path('painel/', views.painel, name='painel'),            # sem sala
    path('painel/<str:sala_nome>/', views.painel, name='painel_sala'),  # com sala

    path('leitos', views.leitos, name='leitos'),
    path('leitos/<str:sala_nome>/', views.leitos, name='leitos_sala'),  # com sala
    path('leito/<str:sala_nome>/<int:id>/editar/', views.editar_leito_page, name='editar_leito_page'),
    path('leito/<str:sala_nome>/<int:id>/deletar/', views.deletar_leito, name='deletar_leito'),
    path('leito/<str:sala_nome>/create_leito/', views.create_leito, name='create_leito'),

    path('centro-cirurgico/', views.centro_cirurgico_view, name='centro_cirurgico'),
    path('salascc/', views.salascc, name='salascc'),
    path('salascc/<str:nome>/editar/', views.editar_sala_cc, name='editar_sala_cc'),  # exemplo
    path('config-salas/', views.config_salas, name='config_salas'),


    path('api/update_leito/<str:sala_nome>/<int:id>/', views.update_leito, name='update_leito'),
    path('api/get_leito/<int:id>/', views.get_leito, name='get_leito'),
    path('get_all_leitos/<str:sala_nome>/', views.get_all_leitos, name='get_all_leitos'),
    path('api/salas-cc/', views.api_salas_cc, name='api_salas_cc'),

]