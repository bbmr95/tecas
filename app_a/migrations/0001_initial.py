# Generated by Django 4.0 on 2021-12-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('autor', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('dir', models.CharField(max_length=100)),
                ('dur', models.IntegerField()),
            ],
        ),
    ]
