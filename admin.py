# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ["title"]
    search_fields = ["title"]
    fieldsets = [
        (_("Content"), {'fields': ["title"]}),
    ]
