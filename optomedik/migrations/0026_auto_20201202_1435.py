# Generated by Django 3.1.3 on 2020-12-02 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0025_auto_20201202_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historia_clinica',
            name='id_medico',
        ),
        migrations.RemoveField(
            model_name='historia_clinica',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='tipo_pago',
        ),
        migrations.RemoveField(
            model_name='pedido_detalle',
            name='id_pedido',
        ),
        migrations.RemoveField(
            model_name='pedido_detalle',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id_clasificacion',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='id_medico',
        ),
        migrations.RemoveField(
            model_name='turnos',
            name='id_paciente',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id_perfil',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='clasificacion',
        ),
        migrations.DeleteModel(
            name='estado',
        ),
        migrations.DeleteModel(
            name='historia_clinica',
        ),
        migrations.DeleteModel(
            name='medico',
        ),
        migrations.DeleteModel(
            name='paciente',
        ),
        migrations.DeleteModel(
            name='pedido',
        ),
        migrations.DeleteModel(
            name='pedido_detalle',
        ),
        migrations.DeleteModel(
            name='perfil',
        ),
        migrations.DeleteModel(
            name='producto',
        ),
        migrations.DeleteModel(
            name='tipo_pago',
        ),
        migrations.DeleteModel(
            name='turnos',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
