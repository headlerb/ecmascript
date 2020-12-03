# Generated by Django 3.1.3 on 2020-12-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('optomedik', '0013_medico_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(max_length=3)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
