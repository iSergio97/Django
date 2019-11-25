# Generated by Django 2.0 on 2019-11-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellidos', models.TextField()),
                ('biografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('estreno', models.IntegerField()),
                ('resumen', models.TextField()),
                ('categoria', models.CharField(max_length=15)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pelis.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellidos', models.TextField()),
                ('fechaNacimiento', models.DateField()),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
    ]
