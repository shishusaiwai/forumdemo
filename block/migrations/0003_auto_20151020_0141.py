# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20151019_0217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '\u7248\u5757', 'verbose_name_plural': '\u7248\u5757'},
        ),
        migrations.AlterField(
            model_name='block',
            name='manager',
            field=models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL),
        ),
    ]
