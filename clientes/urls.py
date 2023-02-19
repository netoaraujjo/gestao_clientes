from django.urls import path

from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.clients, name='clients'),
    path('<int:id>', views.client, name='client_detail'),
    path('new', views.new_client, name='new_client'),
    path('update/<int:id>', views.update_client, name='update_client'),
    path('delete/<int:id>', views.delete_client, name='delete_client'),
]