# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def reviews_main(request):
    return render(
        request, 'book_reviews_app/reviews_main.html', 
    )
