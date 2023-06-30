from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('acercade/', views.acercade, name="acercade"),
    path('login/', views.inicio_sesion, name="login"),
    path('perfil/', views.perfil, name="perfil"),
    path('Registro/', views.registro, name="registro"),
    path('logout/', views.exit, name='exit'),
    path('eliminar/', views.eliminar_usuario, name='eliminar'),
]
