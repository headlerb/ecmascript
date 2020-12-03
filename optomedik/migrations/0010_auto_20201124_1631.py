# Generated by Django 3.1.3 on 2020-11-24 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('optomedik', '0009_auto_20201124_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='clasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clasificacion', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripion', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=64, null=True)),
                ('ciudad', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('valor_total', models.FloatField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_estado', to='optomedik.estado')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_paciente_p', to='optomedik.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripion', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_medico', to='optomedik.medico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_paciente', to='optomedik.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=64)),
                ('armazon', models.CharField(max_length=3)),
                ('id_clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_pedido_id', to='optomedik.clasificacion')),
            ],
        ),
        migrations.CreateModel(
            name='pedido_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_pedido_id', to='optomedik.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_producto_id', to='optomedik.producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_tipo_pago', to='optomedik.tipo_pago'),
        ),
        migrations.CreateModel(
            name='historia_clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('observaciones', models.TextField()),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_medico_hc', to='optomedik.medico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_paciente_hc', to='optomedik.paciente')),
            ],
        ),
    ]
