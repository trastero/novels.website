# Generated by Django 3.2 on 2021-05-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0004_alter_like_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.BooleanField(),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]