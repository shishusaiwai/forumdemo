# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='test',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (-1, '\u5220\u9664'), (10, '\u7cbe\u534e')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (-1, '\u5220\u9664'), (10, '\u7cbe\u534e')]),
        ),
    ]
