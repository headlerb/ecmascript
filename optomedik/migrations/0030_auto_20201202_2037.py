# Generated by Django 3.1.3 on 2020-12-03 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0029_remove_paciente_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo_pago',
            old_name='descripion',
            new_name='descripcion',
        ),
    ]
