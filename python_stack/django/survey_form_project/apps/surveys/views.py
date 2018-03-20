# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):
    return render(request, "surveys/index.html")


def process(request):
    if "submissions" not in request.session:
        request.session['submissions'] = 0
    request.session['submissions'] += 1
    request.session["name"] = request.POST['name']
    request.session["location"] = request.POST['location']
    request.session["language"] = request.POST['language']
    request.session["comment"] = request.POST['comment']
    return redirect("/survey/result")


def result(request):
    return render(request, "surveys/results.html")
