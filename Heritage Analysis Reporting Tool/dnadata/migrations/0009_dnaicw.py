# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0008_auto_20160112_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNAICW',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_match', models.ForeignKey(to='dnadata.DNAMatch', related_name='icw_first_match')),
                ('kit', models.ForeignKey(to='dnadata.DNAKit')),
                ('second_match', models.ForeignKey(to='dnadata.DNAMatch', related_name='icw_second_match')),
            ],
        ),
    ]
