# Generated by Django 4.0.5 on 2022-07-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0026_eventosproximos_fecha_modificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredencialesFacebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.TextField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Credenciales de Facebook',
            },
        ),
    ]
