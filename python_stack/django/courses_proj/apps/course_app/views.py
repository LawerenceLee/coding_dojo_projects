# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from models import Course, Comment, Description
from form_validation import FormValidation


def index(request):
    courses = Course.objects.all()
    return render(request, "course_app/index.html", {"courses": courses})


def process_course(request):
    form = FormValidation(request.POST)
    if form.errors:
        request.session["old_form"] = request.POST
        for err in form.errors:
            messages.add_message(request, messages.ERROR, err)
        return redirect("/")
    else:
        Description.objects.create(desc=request.POST['desc']).save()
        desc = Description.objects.get(desc=request.POST['desc'])
        Course.objects.create(
            name=request.POST['name'],
            desc=desc,
        ).save()
        request.session["old_form"] = ""
        return redirect("/")


def destroy(request, id):
    course = Course.objects.get(id=id)
    return render(request, "course_app/destroy.html", {"course": course})


def process(request, id):
    course = Course.objects.get(id=id)
    description_id = course.desc.id
    course.delete()
    Description.objects.get(id=description_id)
    return redirect("/")
