# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themocheck', '0005_auto_20150504_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='rec_date',
            field=models.DateField(default=b'2015-05-08', serialize=False, primary_key=True),
        ),
    ]
