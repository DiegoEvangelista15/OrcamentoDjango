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
            return redirect('index')
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(
                request, username=username, password=password)
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
            return redirect('cria_conta')
        if not username.strip():
            messages.error(request, 'O campo nome nao pode ficar vazio')
            return redirect('cria_conta')
        if not phone.strip():
            messages.error(request, 'O campo nome nao pode ficar vazio')
            return redirect('cria_conta')
        if not email.strip():
            messages.error(request, 'O campo nome nao pode ficar vazio')
            return redirect('cria_conta')
        if password != password2:
            messages.error(request, 'As senhas nao sao iguais')
            return redirect('cria_conta')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Esse email ja foi cadastrado!!!')
            return redirect('cria_conta')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuario ja existe!!!')
            return redirect('cria_conta')
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        pessoa = Pessoa.objects.create(
            name=complete_name,
            user=username,
            phone=phone,
            email=email,
            area=area
        )
        pessoa.save()
        messages.success(request, 'Cadastro realizado com sucesso!!!')
        return redirect('index')
    return render(request, 'cria_conta.html')


def inserir_dados(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_phone = request.POST['company_phone']
        company_address = request.POST['company_address']
        company_contact = request.POST['company_contact']
        company_mail = request.POST['company_mail']
        company_site = request.POST['company_site']
        user = get_object_or_404(User, pk=request.user.id)

        company = Company.objects.create(
            pessoa=user,
            company_name=company_name,
            company_phone=company_phone,
            company_address=company_address,
            company_contact=company_contact,
            company_mail=company_mail,
            company_site=company_site
        )
        company.save()
        messages.success(request, 'Cadastro realizado com sucesso!!!')
        return redirect('conta_usuario')
    return render(request, 'inserir_dados.html')


def lista_dados(request):
    return render(request, 'lista_dados.html')

def listar_clientes(request):
    return render(request, 'listar_clientes.html')


def criar_orcamento(request):
    return render(request, 'criar_orcamento.html')

