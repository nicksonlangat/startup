# Generated by Django 3.0.8 on 2020-07-05 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200705_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='date_line',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 6, 57, 32, 60024)),
            preserve_default=False,
        ),
    ]
