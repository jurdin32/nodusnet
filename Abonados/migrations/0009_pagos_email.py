# Generated by Django 4.0.5 on 2022-06-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abonados', '0008_pagos_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
