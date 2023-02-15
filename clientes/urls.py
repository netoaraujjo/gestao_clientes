from django.urls import path

from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.clients, name='clients'),
    path('<int:id>/cliente/', views.client, name='client_detail'),
]