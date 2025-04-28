from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leitos', views.leitos, name='leitos'),
    path('get_all_leitos', views.get_all_leitos, name='get_all_leitos'),
]