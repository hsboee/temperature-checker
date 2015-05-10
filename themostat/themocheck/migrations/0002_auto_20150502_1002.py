# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themocheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='date',
            new_name='rec_date',
        ),
        migrations.AddField(
            model_name='theom',
            name='rec_date_index',
            field=models.ForeignKey(default=2, to='themocheck.Date'),
            preserve_default=False,
        ),
    ]
