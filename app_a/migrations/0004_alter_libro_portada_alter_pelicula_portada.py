# Generated by Django 4.0 on 2021-12-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_a', '0003_libro_portada_pelicula_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
