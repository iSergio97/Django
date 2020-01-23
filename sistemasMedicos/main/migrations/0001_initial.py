# Generated by Django 3.0.2 on 2020-01-16 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('numRespuestas', models.IntegerField()),
                ('ultimaRespuesta', models.DateField()),
                ('foroOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Foro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.TextField(unique=True)),
                ('contraseña', models.TextField()),
                ('temasFavoritos', models.ManyToManyField(related_name='TemaFavoritoUsuario', to='main.Tema')),
            ],
        ),
        migrations.CreateModel(
            name='TemaFavoritoUsuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tema')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='tema',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Usuario'),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaHora', models.DateTimeField()),
                ('texto', models.TextField()),
                ('temaOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tema')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
            ],
        ),
    ]