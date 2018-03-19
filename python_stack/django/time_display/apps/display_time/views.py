# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from time import gmtime, strftime


def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request, 'display_time/index.html', context)
