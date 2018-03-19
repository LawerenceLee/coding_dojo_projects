# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "List of blogs"
    return HttpResponse(response)


def new(request):
    return HttpResponse("Create a new blog form")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse("Placeholder to display blog {}".format(number))


def edit(request, number):
    return HttpResponse("Placeholder to edit blog {}".format(number))


def destroy(request, number):
    print("Destroyed Blog #{}".format(number))
    return redirect("/")
