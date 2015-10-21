# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20151021_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='test',
            field=models.IntegerField(),
        ),
    ]
