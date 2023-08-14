# Generated by Django 4.2.1 on 2023-08-13 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('memoria', models.CharField(max_length=100, verbose_name='Memoria')),
                ('version', models.CharField(max_length=100, verbose_name='Versión')),
                ('procesador', models.CharField(max_length=100, verbose_name='Procesador')),
                ('bateria', models.CharField(max_length=100, verbose_name='Batería')),
                ('camara', models.CharField(max_length=100, verbose_name='Cámara')),
                ('image', models.ImageField(upload_to='proyects', verbose_name='Imagen')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizada')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['-created'],
            },
        ),
    ]