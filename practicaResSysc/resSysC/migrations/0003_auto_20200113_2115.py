# Generated by Django 3.0.2 on 2020-01-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resSysC', '0002_auto_20200113_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puntuacion',
            old_name='puntuacion',
            new_name='puntuacionValor',
        ),
    ]
