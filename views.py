# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import MyModel


def mymodel_list(request):
    paginate_by = 24
    qs = MyModel.objects.all()

    paginator = Paginator(qs, paginate_by)
    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page parameter is not an integer, show first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page parameter is out of range, show last existing page.
        page = paginator.page(paginator.num_pages)

    context = {
        'object_list': page,
    }
    return render(request, "{{ app_name }}/mymodel_list.html", context)


def mymodel_details(request, object_id):
    instance = get_object_or_404(MyModel, pk=object_id)
    context = {
        'object': instance,
    }
    return render(request, "{{ app_name }}/mymodel_details.html", context)
