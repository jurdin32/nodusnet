# Generated by Django 4.0.5 on 2022-06-12 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abonados', '0007_alter_pagos_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='referencia',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
