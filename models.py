# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin


@python_2_unicode_compatible
class MyModel(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    is_featured = models.BooleanField(_("Is featured?"), default=False)

    class Meta:
        verbose_name = _("My Model")
        verbose_name_plural = _("My Models")
        ordering = ("title",)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class MyPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("My Plugin Model")
        verbose_name_plural = _("My Plugin Models")
        ordering = ("title",)

    def __str__(self):
        return self.title
