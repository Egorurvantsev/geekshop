# Generated by Django 3.2.12 on 2022-04-27 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 15, 17, 23, 55086, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
