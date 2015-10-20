# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (-1, '\u5220\u9664'), (10, '\u7cbe\u534e')]),
        ),
    ]
