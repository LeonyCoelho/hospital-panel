
import app_painel_hegv
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app_painel_hegv.urls"))
]
