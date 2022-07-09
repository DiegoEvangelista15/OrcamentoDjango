from django.shortcuts import render

# Create your views here.

def index(request):
    #TODO criar formulario para acesso
    return render(request, 'index.html')

def conta_usuario(request):
    #TODO criar e arrumar acesso de acordo com user
    return render(request, 'main_contausuario.html')

def cria_conta(request):
    #TODO criar o formulario e view para criar conta de user 
    return render(request, 'cria_conta.html')

def inserir_dados(request):
    return render(request, 'inserir_dados.html')

def lista_dados(request):
    return render(request, 'lista_dados.html')

def criar_orcamento(request):
    return render(request, 'criar_orcamento.html')