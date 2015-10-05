# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actuaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='actuary',
            name='country',
            field=models.ForeignKey(default=0, to='actuaries.Country'),
            preserve_default=False,
        ),
    ]
