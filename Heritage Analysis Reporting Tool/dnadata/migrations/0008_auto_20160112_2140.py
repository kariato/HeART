# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0007_auto_20160110_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnamatch',
            name='YDNAHaplogroup',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnamatch',
            name='mtDNAHaplogroup',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnamatch',
            name='name',
            field=models.CharField(default=1, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnamatch',
            name='notes',
            field=models.CharField(default=1, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnamatch',
            name='resultID2',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
