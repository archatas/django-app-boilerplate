# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


def {{ app_name }}(request):
    from .models import MyModel
    d = {
        'random_mymodels': MyModel.objects.order_by("?")[:3],
        }
    return d
