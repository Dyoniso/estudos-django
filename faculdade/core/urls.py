from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.novo_produto, name='novo_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
]