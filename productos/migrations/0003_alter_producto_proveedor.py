# Generated by Django 5.1.6 on 2025-03-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_categoria_detalles_producto_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ManyToManyField(blank=True, to='productos.proveedor'),
        ),
    ]
