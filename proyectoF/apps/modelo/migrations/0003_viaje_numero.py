# Generated by Django 3.1.4 on 2021-02-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_auto_20210224_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='numero',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]