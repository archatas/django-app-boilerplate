# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import template
from ..models import MyModel

register = template.Library()

@register.inclusion_tag('{{ app_name }}/includes/latest_mymodel_items.html', takes_context=True)
def show_latest_mymodel_items(context):
    queryset = MyModel.objects.all()[:3]
    context['latest_mymodel_items'] = queryset
    return context
