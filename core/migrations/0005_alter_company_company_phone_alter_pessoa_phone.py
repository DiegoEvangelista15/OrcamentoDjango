# Generated by Django 4.0.6 on 2022-07-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pessoa_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
