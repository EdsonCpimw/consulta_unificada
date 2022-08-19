# Generated by Django 4.1 on 2022-08-18 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pad', '0002_viewtramitacaocorporativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewtramitacaocorporativo',
            name='data_envio',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='viewtramitacaocorporativo',
            name='sigla_orgao',
            field=models.CharField(max_length=6),
        ),
    ]