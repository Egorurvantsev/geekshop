# Generated by Django 3.2.12 on 2022-04-18 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='age',
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 20, 15, 50, 9, 718973, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
