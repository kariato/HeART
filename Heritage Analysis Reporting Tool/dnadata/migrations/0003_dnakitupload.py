# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0002_auto_20151215_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNAKitUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('filename', models.CharField(max_length=300)),
                ('uploadType', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=300)),
                ('log', models.CharField(max_length=300)),
                ('uploaded', models.DateTimeField()),
                ('kit', models.ForeignKey(to='dnadata.DNAKit')),
            ],
        ),
    ]
