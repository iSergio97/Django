# Generated by Django 2.0 on 2019-11-25 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('idPelicula', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fechaEstreno', models.DateField()),
                ('IMDbURL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendacionPelis.Pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('codigoPostal', models.IntegerField()),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendacionPelis.Ocupacion')),
                ('puntuaciones', models.ManyToManyField(through='recomendacionPelis.Puntuacion', to='recomendacionPelis.Pelicula')),
            ],
        ),
        migrations.AddField(
            model_name='puntuacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendacionPelis.Usuario'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='pelicula',
            field=models.ManyToManyField(to='recomendacionPelis.Pelicula'),
        ),
    ]
