from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Criacao', auto_now_add=True)  # so eh colocado na add
    modificado = models.DateField('Atualizacao', auto_now=True)  # sempre que modifica, ele muda
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
        
class Company(Base):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(("Nome da Empresa"), max_length=200)
    company_phone = models.CharField(max_length=50)
    company_address = models.CharField(("Endereço da Empresa"), max_length=300)
    company_contact = models.CharField(("Contato da Empresa"), max_length=100)
    company_mail = models.EmailField()
    company_site = models.CharField(("Site da Empresa"), max_length=200)
    
    def __str__(self) -> str:
        return self.company_name
    
class Pessoa(Base):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField() 
    area = models.CharField(max_length=50)    
    
    def __str__(self) -> str:
        return self.name
    
class Item(Base):
    item = models.CharField(max_length=255)
    description = models.TextField(max_length=650)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    discount = models.FloatField()  
    
    
    def __str__(self) -> str:
        return self.item    
   
class Orcamento(Base):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    pessoa_info = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    payment_terms = models.CharField(max_length=250)
    delivery_time = models.PositiveIntegerField()
    incoterms = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.pessoa_info, self.empresa)  
    