# Generated by Django 3.0.8 on 2020-07-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_application_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='recruiter_email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]