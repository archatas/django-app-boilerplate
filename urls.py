# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.mymodel_list, name='mymodel_list'),
    url(r'^featured/$', views.mymodel_list, {'featured': True}, name='featured_mymodel_list'),
    url(r'^(?P<object_id>\d+)/$', views.mymodel_details, name='mymodel_details'),
]
