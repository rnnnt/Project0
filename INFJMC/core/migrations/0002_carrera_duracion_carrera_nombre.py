# Generated by Django 5.0.4 on 2024-05-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='duracion',
            field=models.IntegerField(default=1, verbose_name='duracion'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(default='Nombre por defecto', max_length=80, verbose_name='nombre'),
            preserve_default=False,
        ),
    ]