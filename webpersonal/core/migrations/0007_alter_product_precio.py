# Generated by Django 4.2.1 on 2023-08-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]