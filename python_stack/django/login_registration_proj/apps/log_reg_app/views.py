# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from models import User
from form_validation import FormValidation


# /
def index(request):
    if request.method == "POST":
        form = FormValidation(request.POST)

        if form.errors:
            for message in form.errors:
                messages.error(request, message)
            return render(
                request, "log_reg_app/index.html", {"old_form": request.POST}
            )
        else:
            if not User.objects.filter(email=request.POST['email']):
                hashed_pw = bcrypt.hashpw(
                    str(request.POST['password']).encode(), bcrypt.gensalt()
                )
                User.objects.create(
                    first_name=str(request.POST['first_name']),
                    last_name=str(request.POST['last_name']),
                    # birthdate=request.POST['birthdate'],
                    email=str(request.POST["email"]),
                    password=hashed_pw,
                ).save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Your user info was successfully submitted"
                )
                return redirect("/login")
            else:
                messages.error(request, "That user already exists")

    return render(request, 'log_reg_app/index.html', {"old_form": request.POST})


#  /login
def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
        except User.DoesNotExist:
            messages.error(request, "Email does not exist")
            return redirect("/login")
        else:
            passed_pswd = request.POST['password']
            if bcrypt.checkpw(passed_pswd.encode(), user.password.encode()):
                request.session['is_logged_in'] = True
                request.session["first_name"] = user.first_name
                messages.success(request, "Successful Login")
                return redirect("/success")

        messages.error(request, "Either Email or Password is not correct")
        return redirect("/login")

    return render(request, "log_reg_app/login.html")


#  /success
def success(request):
    return render(request, "log_reg_app/success.html")