# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):
    if 'total_spending' not in request.session:
        request.session['total_num_items'] = 0
        request.session['total_spending'] = 0
        request.session['bill'] = 0
    else:
        request.session['bill'] = 0

    request.session['items'] = [
        {
            'id': 1,
            'name': "Dojo T-Shirt",
            'price': 19.99,
        },
        {
            'id': 2,
            'name': "Dojo Sweater",
            'price': 4.99,
        },
        {
            'id': 3,
            'name': "Dojo Cup",
            'price': 4.99,
        },
        {
            'id': 4,
            'name': "Algorithm Book",
            'price': 49.99,
        }
    ]
    return render(request, "shopping_cart/index.html")


def process(request):
    for item in request.session['items']:
        print(item['id'], request.POST['item_id'])
        if item['id'] == float(request.POST['item_id']):
            request.session['total_num_items'] += int(request.POST['quantity'])
            request.session['bill'] = int(request.POST['quantity']) * float(item['price'])
            request.session['total_spending'] += float(request.session["bill"])
    return redirect("/thank_you")


def thank_you(request):
    return render(request, "shopping_cart/thank_you.html")