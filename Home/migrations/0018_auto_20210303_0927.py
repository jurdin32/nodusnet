# Generated by Django 3.1.4 on 2021-03-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_auto_20210303_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalles',
            name='icono',
            field=models.CharField(max_length=20),
        ),
    ]
