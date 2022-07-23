from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conta_usuario/', views.conta_usuario, name='conta_usuario'),
    path('cria_conta/', views.cria_conta, name='cria_conta'),
    path('inserir_dados/', views.inserir_dados, name='inserir_dados'),
    path('lista_dados/', views.lista_dados, name='lista_dados'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('listar_itens/', views.listar_itens, name='listar_itens'),
    path('criar_orcamento/', views.criar_orcamento, name='criar_orcamento'),
    path('criar_itens/', views.criar_itens, name='criar_itens'),
    path('logout', views.logout, name='logout'),
    path('atualiza_item/', views.atualiza_item, name='atualiza_item'),
    path('edita_item/<int:item_id>', views.edita_item, name='edita_item'),
    path('deleta_item/<int:item_id>', views.deleta_item, name='deleta_item'),
]
