# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themocheck', '0004_auto_20150504_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='id',
        ),
        migrations.AlterField(
            model_name='date',
            name='rec_date',
            field=models.DateField(default=b'2015-05-04', serialize=False, primary_key=True),
        ),
    ]
