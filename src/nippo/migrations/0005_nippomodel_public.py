# Generated by Django 5.1.7 on 2025-03-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0004_nippomodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='nippomodel',
            name='public',
            field=models.BooleanField(default=False, verbose_name='公開する'),
        ),
    ]
