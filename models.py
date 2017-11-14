# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MyModel(models.Model):
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("My Model")
        verbose_name_plural = _("My Models")
        ordering = ("title",)

    def __str__(self):
        return self.title
