# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150619_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstdb',
            name='email',
            field=models.EmailField(max_length=25, blank=True),
        ),
        migrations.AddField(
            model_name='firstdb',
            name='ip',
            field=models.GenericIPAddressField(default=b'0.0.0.0'),
        ),
    ]
