# Generated by Django 4.1.3 on 2024-07-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_marca_remove_producto_unidad_de_medida_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
