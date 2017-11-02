# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = '{{ app_name }}'
    verbose_name = _("My App")

    def ready(self):
        pass
