# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {"random_word": get_random_string(length=14).upper()}
    if "counter" not in request.session:
        request.session['counter'] = 0

    request.session['counter'] += 1
    return render(request, "rand_word_gen/index.html", context)


def reset_attempts(request):
    if "counter" in request.session:
        request.session['counter'] = 0
    return redirect("/random_word")
