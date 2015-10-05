# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('age', models.IntegerField()),
                ('mx', models.DecimalField(max_digits=6, decimal_places=5)),
                ('qx', models.DecimalField(max_digits=6, decimal_places=5)),
                ('ax', models.DecimalField(max_digits=3, decimal_places=2)),
                ('lx', models.IntegerField()),
                ('dx', models.IntegerField()),
                ('Lx', models.IntegerField()),
                ('Tx', models.IntegerField()),
                ('ex', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
