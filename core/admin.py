from django.contrib import admin
from .models import Company, Pessoa, Item, Orcamento

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'company_name','criado')
    
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('name', 'user','criado')
    
@admin.register(Item)
class PItemAdmin(admin.ModelAdmin):
    list_display = ('item','criado', 'modificado')
    
@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'pessoa_info','criado','modificado')