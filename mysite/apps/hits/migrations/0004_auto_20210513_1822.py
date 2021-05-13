# Generated by Django 3.2 on 2021-05-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0003_alter_hitslog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklistip',
            name='ip',
            field=models.CharField(default='127.0.0.1', max_length=45, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blacklistua',
            name='user_agent',
            field=models.CharField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]