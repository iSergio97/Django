# Generated by Django 2.0 on 2019-12-02 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191202_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='lenguages',
            new_name='lenguajes',
        ),
    ]
