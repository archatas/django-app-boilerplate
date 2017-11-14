# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import MyPluginModel


class MyPluginModelPlugin(CMSPluginBase):
    model = MyPluginModel
    name = _("My Plugin")
    render_template = "cms/plugins/my_plugin_model.html"

    fieldsets = (
        (_("Main Content"), {'fields': ["title"], 'classes': ["collapse open"]}),
    )

plugin_pool.register_plugin(MyPluginModelPlugin)