# Generated by Django 3.2.7 on 2021-10-13 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_auto_20211004_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.RemoveField(
            model_name='guia',
            name='tipo_turismo',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='tipo_turismo',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='tipo_turismo',
        ),
        migrations.AddField(
            model_name='plan',
            name='cant_personas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='nombre_plan',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Plan'),
        ),
        migrations.AddField(
            model_name='plan',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='valor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Fullname'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Guia',
        ),
        migrations.DeleteModel(
            name='Lugar',
        ),
        migrations.DeleteModel(
            name='TipoTurismo',
        ),
    ]
