# Generated by Django 4.0.5 on 2022-06-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfiguracionEmail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envioemail',
            name='password',
            field=models.CharField(default='Urdin32**', max_length=200),
        ),
        migrations.AddField(
            model_name='envioemail',
            name='use_tls',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='envioemail',
            name='usuario',
            field=models.CharField(default='urdin-23@live.com', max_length=200),
        ),
    ]
