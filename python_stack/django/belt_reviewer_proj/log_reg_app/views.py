# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages

from models import User
from form_validation import FormValidation


# /register
def register(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    elif request.session["is_logged_in"] is True:
        messages.error(request, "You are aready logged in")
        return redirect("/success")

    if request.method == "POST":
        form = FormValidation(request.POST)

        if form.errors:
            for message in form.errors:
                messages.error(request, message)
            return render(
                request, "log_reg_app/login_reg.html",
                {"old_form": request.POST}
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

    return render(
        request, 'log_reg_app/login_reg.html', {"old_form": request.POST}
    )


#  /login
def login(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    elif request.session["is_logged_in"] is True:
        messages.error(request, "You are aready logged in")
        return redirect("/success")
    elif request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
        except User.DoesNotExist:
            messages.error(request, "Email does not exist")
        else:
            passed_pswd = request.POST['password']
            if bcrypt.checkpw(passed_pswd.encode(), user.password.encode()):
                request.session['is_logged_in'] = True
                request.session['user_id'] = user.id
                request.session["first_name"] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = user.email
                request.session['created_at'] = user.created_at.strftime(
                    "%I:%M %p %B $d, %Y"
                )
                request.session['changed_at'] = user.changed_at.strftime(
                    "%I:%M %p %B $d, %Y"
                )
                messages.success(request, "Successful Login")
                return redirect("/success")
            else:
                messages.error(
                    request, "Either Email or Password or both is not correct"
                )

    return render(
            request, "log_reg_app/login_reg.html", {"old_form": request.POST}
        )


#  /success
def success(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
    elif request.session["is_logged_in"] is True:
        return redirect("/books")

    messages.error(request, "You have not logged in yet")
    return redirect("/login")


def logoff(request):
    if 'is_logged_in' not in request.session:
        request.session['is_logged_in'] = False
        messages.error(request, "You have not logged in yet")
    elif request.session["is_logged_in"] is True:
        messages.success(request, "You successfully logged off")
        keys_vals_to_del = [
            "is_logged_in", "first_name", "last_name", "email",
            "created_at", "changed_at"
        ]
        for key in keys_vals_to_del:
            del request.session[key]
    else:
        messages.error(request, "You have not logged in yet")

    return redirect("/login")
