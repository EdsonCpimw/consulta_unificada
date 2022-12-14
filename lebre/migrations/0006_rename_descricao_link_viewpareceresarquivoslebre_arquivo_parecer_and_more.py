# Generated by Django 4.1 on 2022-08-21 22:45

from django.db import migrations, models
import lebre.models


class Migration(migrations.Migration):

    dependencies = [
        ('lebre', '0005_rename_viewdespacho_viewdespacholebre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewpareceresarquivoslebre',
            old_name='descricao_link',
            new_name='arquivo_parecer',
        ),
        migrations.AddField(
            model_name='viewnotificacoeslebre',
            name='documento_notificacao',
            field=models.FileField(default=278, upload_to=lebre.models.upload_notificacao_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewvistorialebre',
            name='documento_vistoria',
            field=models.FileField(default=1998, upload_to=lebre.models.upload_vistoria_path),
            preserve_default=False,
        ),
    ]
