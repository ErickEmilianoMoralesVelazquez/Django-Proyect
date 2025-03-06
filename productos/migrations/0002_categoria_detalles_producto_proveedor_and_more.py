# Generated by Django 5.1.6 on 2025-03-06 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=400)),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='detalles_producto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.detalles_producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ManyToManyField(blank=True, null=True, to='productos.proveedor'),
        ),
    ]
