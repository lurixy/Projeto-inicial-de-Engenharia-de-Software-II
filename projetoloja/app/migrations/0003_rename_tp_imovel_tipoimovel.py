# Generated by Django 5.0.3 on 2024-03-13 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bairro_cargo_cidade_status_tipo_tipologradouro_uf_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='tp',
            new_name='tipoimovel',
        ),
    ]