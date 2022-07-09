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
    company_phone = models.IntegerField()
    company_address = models.CharField(("Endereço da Empresa"), max_length=300)
    company_contact = models.CharField(("Contato da Empresa"), max_length=100)
    company_mail = models.EmailField()
    company_site = models.CharField(("Site da Empresa"), max_length=200)
    
    def __str__(self) -> str:
        return self.company_name
    
class Pessoa(Base):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()     
    
    def __str__(self) -> str:
        return self.name