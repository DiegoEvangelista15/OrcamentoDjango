from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def conta_usuario(request):
    return render(request, 'main_contausuario.html')

def cria_conta(request):
    return render(request, 'cria_conta.html')

def inserir_dados(request):
    return render(request, 'inserir_dados.html')

def lista_dados(request):
    return render(request, 'lista_dados.html')

def criar_orcamento(request):
    return render(request, 'criar_orcamento.html')