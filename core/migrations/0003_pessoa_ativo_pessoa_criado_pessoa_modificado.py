# Generated by Django 4.0.6 on 2022-07-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='criado',
            field=models.DateField(auto_now_add=True, verbose_name='Criacao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Atualizacao'),
        ),
    ]
