# Generated by Django 3.1.3 on 2020-12-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0038_auto_20201203_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='asistio',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=20),
        ),
    ]
