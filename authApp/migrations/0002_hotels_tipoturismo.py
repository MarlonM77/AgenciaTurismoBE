# Generated by Django 3.2.7 on 2021-10-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Name')),
                ('ubicacion', models.CharField(max_length=30, verbose_name='ubicacion')),
                ('json_fotos', models.CharField(max_length=30, verbose_name='json_fotos')),
                ('contacto', models.CharField(max_length=30, verbose_name='telefono')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTurismo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_turismo', models.CharField(max_length=30, verbose_name='tipo_turismo')),
            ],
        ),
    ]