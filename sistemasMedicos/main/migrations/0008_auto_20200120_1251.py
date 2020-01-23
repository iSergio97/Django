# Generated by Django 3.0.2 on 2020-01-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200116_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tema',
            name='foroOrigen',
        ),
        migrations.AddField(
            model_name='tema',
            name='category',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='temaOrigen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tema'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Usuario'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Usuario'),
        ),
        migrations.AlterField(
            model_name='temafavoritousuario',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Tema'),
        ),
        migrations.AlterField(
            model_name='temafavoritousuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Usuario'),
        ),
        migrations.DeleteModel(
            name='Foro',
        ),
    ]