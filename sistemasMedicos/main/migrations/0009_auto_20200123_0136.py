# Generated by Django 3.0.2 on 2020-01-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200120_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tema',
            name='numRespuestas',
        ),
        migrations.RemoveField(
            model_name='tema',
            name='ultimaRespuesta',
        ),
        migrations.RemoveField(
            model_name='tema',
            name='usuario',
        ),
        migrations.AddField(
            model_name='tema',
            name='link',
            field=models.TextField(default=''),
        ),
    ]