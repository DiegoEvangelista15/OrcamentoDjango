from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from core.models import Pessoa, Company, Item, Orcamento
from core.forms import ItemForm, OrcamentoForm
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
    # TODO listar dados por user e superuser verifica tudo
    return render(request, 'lista_dados.html')


def listar_clientes(request):
    # TODO falta colocar a função dos números e paginação
    clientes = Company.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})


def criar_orcamento(request):
    # TODO colocar as infos  e seguir com o preechimento do orcamento
    form = OrcamentoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            empresa = get_object_or_404(Company, pk=request.POST['empresa'])
            payment_terms = request.POST['payment_terms']
            delivery_time = request.POST['delivery_time']
            incoterms = request.POST['incoterms']
            user = get_object_or_404(User, pk=request.user.id)
            pessoa_info = get_object_or_404(Pessoa, pk=request.user.id)
            item = Item.objects.filter(id=request.POST['item'])
            # corrigir esse item, nao esta pegando os valores

            orcamento = Orcamento.objects.create(
                pessoa=user,
                pessoa_info=pessoa_info,
                empresa=empresa,
                item=item,
                payment_terms=payment_terms,
                delivery_time=delivery_time,
                incoterms=incoterms,
            )
            orcamento.save()
            messages.success(request, 'Cadastro realizado com sucesso!!!')
            return redirect('criar_itens')
        else:
            messages.error(request, 'Falha ao preencher!!!')
            return redirect('criar_orcamento')

    return render(request, 'criar_orcamento.html', {'form': form})


def listar_itens(request):
    # TODO colocar paginação e função dos botões
    itens = Item.objects.all()
    return render(request, 'listar_itens.html', {'itens': itens})


def criar_itens(request):
    form = ItemForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            item = request.POST['item']
            description = request.POST['description']
            quantity = request.POST['quantity']
            price = request.POST['price']
            discount = request.POST['discount']

            item = Item.objects.create(
                item=item,
                description=description,
                quantity=quantity,
                price=price,
                discount=discount,
            )
            item.save()
            messages.success(request, 'Cadastro realizado com sucesso!!!')
            return redirect('conta_usuario')

        else:
            messages.error(request, 'Falha ao preencher!!!')
            return redirect('criar_itens')

    return render(request, 'criar_itens.html', {'form': form})


def edita_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_editar = {'item': item}
    return render(request, 'edita_item.html', item_editar)


def deleta_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('listar_itens')


def atualiza_item(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        i = Item.objects.get(pk=item_id)  # take all information
        i.item = request.POST['item']
        i.description = request.POST['description']
        i.quantity = request.POST['quantity']
        i.price = request.POST['price']
        i.discount = request.POST['discount']
        i.save()
        return redirect('listar_itens')
