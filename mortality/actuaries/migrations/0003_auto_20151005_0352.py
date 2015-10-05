# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actuaries', '0002_auto_20150927_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='actuaries.Region', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='actuary',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AddField(
            model_name='actuary',
            name='region',
            field=models.ForeignKey(default=1, to='actuaries.Region'),
            preserve_default=False,
        ),
    ]
