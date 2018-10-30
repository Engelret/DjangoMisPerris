from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('registroPersona/',views.registroPersona, name="registroPersona"),
    path('registroPersona/crearPersona',views.crearPersona, name="crearPersona"),
    path('login',views.login, name="login")
]

