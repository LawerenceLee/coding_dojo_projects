# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from models import User
from form_validation import FormValidation


# /users'
def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {"users": users})


# /users/new
def new_user(request):
    return render(request, 'users/create_user.html')


# /users/create
def create_user(request):
    form = FormValidation(request.POST)
    if not form.errors:
        User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
            )
        user = User.objects.get(email=request.POST['email'])
        messages.add_message(
            request, messages.INFO, "Successfully Created User")
        request.session['past_form'] = ""
        return redirect("/users/{}".format(user.id))
    else:
        for err in form.errors:
            print(err)
            messages.error(request, err)

        request.session['past_form'] = request.POST
        return redirect(reverse('users:new'))


# /users/<int:id>/edit
def edit_user(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/update.html', {"user": user})


# /users/update
def update_user(request, id):
    user = User.objects.get(id=request.POST["user_id"])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    messages.add_message(
        request, messages.INFO,
        "Successfully Made the Changes You asked for")
    return redirect("/users/{}".format(request.POST["user_id"]))


# /users/<int:id>/delete
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.add_message(request, messages.INFO, "Deleted User")
    return redirect("/users")


# /users/<int:id>
def user_by_id(request, id):
    user = User.objects.get(id=id)
    date_time = user.created_at.strftime("%B %d %Y")
    return render(
        request, "users/user.html",
        {"user": user, "date_time": date_time})
