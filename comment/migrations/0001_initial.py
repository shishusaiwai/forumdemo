# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_remove_article_test'),
        ('block', '0003_auto_20151020_0141'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_comment_id', models.IntegerField(default=0, verbose_name='\u56de\u590d\u8bc4\u8bba')),
                ('content', models.CharField(max_length=10000, verbose_name='\u5185\u5bb9')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (-1, '\u5220\u9664')])),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(verbose_name='\u6240\u5c5e\u6587\u7ae0', to='article.Article')),
                ('block', models.ForeignKey(verbose_name='\u6240\u5c5e\u7248\u5757', to='block.Block')),
                ('owner', models.ForeignKey(verbose_name='\u8bc4\u8bba\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
