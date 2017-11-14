# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class MyAppMenu(CMSAttachMenu):
    name = _("My App Menu")

    def get_nodes(self, request):
        nodes = [
            NavigationNode(
                _("All"),
                reverse("mymodel_list"),
                1,
            ),
            NavigationNode(
                _("Featured"),
                reverse("featured_mymodel_list"),
                2,
            ),
        ]
        return nodes

menu_pool.register_menu(MyAppMenu)