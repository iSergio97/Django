# Generated by Django 3.0.2 on 2020-01-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resSysC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='numEpisodios',
            field=models.TextField(),
        ),
    ]
