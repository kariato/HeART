# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0003_dnakitupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnakitupload',
            name='files',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
