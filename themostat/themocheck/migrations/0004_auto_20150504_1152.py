# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themocheck', '0003_auto_20150503_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theom',
            name='id',
        ),
        migrations.AlterField(
            model_name='date',
            name='rec_date',
            field=models.DateField(default=b'20150504'),
        ),
        migrations.AlterField(
            model_name='theom',
            name='time',
            field=models.TimeField(serialize=False, primary_key=True),
        ),
    ]
