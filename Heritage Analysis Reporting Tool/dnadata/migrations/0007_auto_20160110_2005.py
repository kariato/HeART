# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0006_auto_20160110_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnakitupload',
            name='files',
        ),
        migrations.AddField(
            model_name='dnakitupload',
            name='filesInfo',
            field=models.FileField(upload_to='documents/%Y/%m/%d', blank=True),
        ),
    ]
