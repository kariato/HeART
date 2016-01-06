# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DNAKits',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('resultSet', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DNAMatches',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('resultSet', models.ForeignKey(to='dnadata.DNAKits')),
            ],
        ),
        migrations.CreateModel(
            name='DNASegment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('chromosome', models.IntegerField()),
                ('startLocation', models.IntegerField()),
                ('endLocation', models.IntegerField()),
                ('centimorgans', models.FloatField()),
                ('matchingSnps', models.FloatField()),
                ('matchname', models.ForeignKey(to='dnadata.DNAMatches')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('familyName', models.CharField(max_length=300)),
                ('user', models.ForeignKey(related_name='DNAMatches_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dnakits',
            name='family',
            field=models.ForeignKey(to='dnadata.Family'),
        ),
    ]
