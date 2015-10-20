# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Block(models.Model):
    name = models.CharField(u"名字", max_length=30)
    desc = models.CharField(u"描述", max_length=150)
    manager = models.ForeignKey(User, verbose_name="管理员")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"版块"
        verbose_name_plural = u"版块"
