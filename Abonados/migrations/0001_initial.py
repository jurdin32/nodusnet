# Generated by Django 4.0.5 on 2022-06-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=13)),
                ('nombres', models.CharField(default=' ', max_length=60)),
                ('razon_social', models.CharField(default=' ', max_length=300)),
            ],
        ),
    ]
