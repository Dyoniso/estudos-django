from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='pedidos'),
    path('cadastro/pedido/', views.cadastro_pedido, name='cadastro_pedido'),
    path('login/', views.login, name='login'),
    path('login/efetuar', views.efetuar_login, name='efetuar_login'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo', views.novo_produto, name='novo_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:pk>/', views.deletar_produto, name='deletar_produto'),
]