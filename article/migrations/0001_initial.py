# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0003_auto_20151020_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.CharField(max_length=10000, verbose_name='\u5185\u5bb9')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(verbose_name='\u6240\u5c5e\u7248\u5757', to='block.Block')),
                ('owner', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
