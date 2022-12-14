# Generated by Django 4.1 on 2022-08-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewTramitacaoCorporativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_processo', models.CharField(max_length=100)),
                ('orgao_destino', models.CharField(max_length=100)),
                ('data_envio', models.DateField(auto_now_add=True)),
                ('sigla_orgao', models.CharField(max_length=4)),
                ('observacao', models.TextField()),
            ],
            options={
                'db_table': 'tb_view_tramitacao',
                'ordering': ['id'],
            },
        ),
    ]
