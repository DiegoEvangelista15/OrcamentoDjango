# Generated by Django 4.0.6 on 2022-07-10 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_company_company_phone_alter_pessoa_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('item', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=650)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('payment_terms', models.CharField(max_length=250)),
                ('delivery_time', models.PositiveIntegerField()),
                ('incoterms', models.CharField(max_length=250)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
                ('item', models.ManyToManyField(to='core.item')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pessoa_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
