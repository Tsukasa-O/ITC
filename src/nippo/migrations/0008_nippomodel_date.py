# Generated by Django 5.1.7 on 2025-03-26 13:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0007_alter_nippomodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='nippomodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
