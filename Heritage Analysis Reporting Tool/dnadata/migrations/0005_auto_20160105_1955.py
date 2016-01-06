# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0004_dnakitupload_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(upload_to='file_folder/', default='file_folder/None/no-file.csv')),
            ],
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='filename',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='files',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='log',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='status',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='uploadType',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='dnakitupload',
            name='uploaded',
            field=models.DateTimeField(blank=True),
        ),
    ]
