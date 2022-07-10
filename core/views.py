from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from core.models import Pessoa, Company
from openpyxl import Workbook

# Create your views here.


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if email == '' or password == '':
            return redirect ('index')
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('conta_usuario')   
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def conta_usuario(request):
    return render(request, 'main_contausuario.html')


def cria_conta(request):
    if request.method == 'POST':
        complete_name = request.POST['complete_name']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        area = request.POST['area']
        if not complete_name.strip():
                messages.error(request, 'O campo nome nao pode ficar vazio')
                return redirect ('cria_conta')
  
    return render(request, 'cria_conta.html')


def inserir_dados(request):
    return render(request, 'inserir_dados.html')


def lista_dados(request):
    return render(request, 'lista_dados.html')


def criar_orcamento(request):
    return render(request, 'criar_orcamento.html')
