# Generated by Django 3.1.3 on 2020-11-24 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optomedik', '0007_estado_historia_clinica_pedido_tipo_pago'),
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
    ]
