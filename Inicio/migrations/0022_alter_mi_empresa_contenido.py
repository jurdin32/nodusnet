# Generated by Django 4.0.5 on 2022-06-11 02:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0021_mi_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mi_empresa',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]