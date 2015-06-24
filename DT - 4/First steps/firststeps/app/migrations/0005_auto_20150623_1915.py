# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_firstdb_txtfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstdb',
            name='txtfile',
            field=models.FileField(upload_to=b'C:\\Users\\Prajwal K R\\Desktop\\First steps\\firststeps/File Uploads/'),
        ),
    ]
