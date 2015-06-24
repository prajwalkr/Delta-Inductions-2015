# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstdb',
            name='id',
        ),
        migrations.AlterField(
            model_name='firstdb',
            name='name',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
