# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20151021_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='test',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
    ]
