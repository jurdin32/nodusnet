# Generated by Django 4.0.5 on 2022-06-11 01:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0020_alter_configuracion_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mi_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
    ]