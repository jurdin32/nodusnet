# Generated by Django 4.0.5 on 2022-06-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abonados', '0003_pagos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='fecha',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagos',
            name='fecha_pago',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
