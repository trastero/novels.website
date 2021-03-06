# Generated by Django 3.2 on 2021-05-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Distro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, unique=True)),
                ('slug', models.SlugField(max_length=180, unique=True)),
                ('type', models.CharField(choices=[('LN', 'Light novel'), ('WN', 'Web novel')], default='LN', max_length=2, verbose_name='Tipo')),
                ('structure', models.CharField(choices=[('VOL', 'Volumes'), ('ARC', 'Arcs'), ('CHA', 'Chapters')], default='VOL', max_length=3, verbose_name='Estructura')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
