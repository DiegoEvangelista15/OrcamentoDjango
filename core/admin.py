from django.contrib import admin
from .models import Company, Pessoa

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'company_name','criado')
    
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','criado')