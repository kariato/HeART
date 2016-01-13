# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0005_auto_20160105_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnakitupload',
            name='files',
            field=models.FileField(blank=True, upload_to='scrap'),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]
