# Generated by Django 3.0.2 on 2020-01-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiqueta',
            name='idTag',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]