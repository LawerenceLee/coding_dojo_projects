# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, redirect


def index(request):
    return render(request, "words/index.html")


def process(request):
    if 'words' not in request.session:
        request.session["words"] = []
    word = {
        "word": request.POST['new_word'],
        "color": request.POST['color'],
        "time_date": datetime.now().strftime("%I:%M:%S%p, %B %d %Y")
    }
    if 'big' not in request.POST:
        word['big'] = 'not_big'
    else:
        word['big'] = 'big'
    saved_list = request.session['words']
    saved_list.append(word)
    request.session['words'] = saved_list
    return redirect("/session_words")


def clear_session(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/session_words")

