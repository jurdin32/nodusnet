# Generated by Django 3.0.9 on 2021-02-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_pymes_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nosotros',
            options={'verbose_name_plural': '1.3 Nosotros'},
        ),
        migrations.AddField(
            model_name='datosprincipales',
            name='whatsapp',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
