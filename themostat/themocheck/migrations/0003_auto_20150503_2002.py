# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themocheck', '0002_auto_20150502_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='rec_date',
            field=models.DateField(default=b'20150503'),
        ),
        migrations.AlterField(
            model_name='theom',
            name='time',
            field=models.TimeField(),
        ),
    ]
