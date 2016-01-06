# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnadata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNAKit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('resultSet', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('family', models.ForeignKey(to='dnadata.Family')),
            ],
        ),
        migrations.CreateModel(
            name='DNAMatch',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fullName', models.CharField(max_length=300)),
                ('firstName', models.CharField(max_length=300)),
                ('middleName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('matchDate', models.DateField()),
                ('relationshipRange', models.CharField(max_length=300)),
                ('suggestedRelationship', models.CharField(max_length=300)),
                ('sharedCM', models.FloatField()),
                ('longestBlock', models.FloatField()),
                ('knownRelationship', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('ancestralSurnames', models.CharField(max_length=3000)),
                ('resultSet', models.ForeignKey(to='dnadata.DNAKit')),
            ],
        ),
        migrations.RemoveField(
            model_name='dnakits',
            name='family',
        ),
        migrations.RemoveField(
            model_name='dnamatches',
            name='resultSet',
        ),
        migrations.AlterField(
            model_name='dnasegment',
            name='matchname',
            field=models.ForeignKey(to='dnadata.DNAMatch'),
        ),
        migrations.DeleteModel(
            name='DNAKits',
        ),
        migrations.DeleteModel(
            name='DNAMatches',
        ),
    ]
