# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import MyModel

class MyModelForm(models.ModelForm):
    class Meta:
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        