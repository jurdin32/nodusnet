# Generated by Django 4.0.5 on 2022-06-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abonados', '0005_pagos_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='fecha_pago',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]