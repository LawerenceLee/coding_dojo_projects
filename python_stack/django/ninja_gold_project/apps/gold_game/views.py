# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from classes import Farm, Cave, Casino, House


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    return render(request, 'gold_game/index.html')


def process_money(request):
    if request.POST['building'] == 'farm':
        farm = Farm()
        request.session['gold'] += farm.gold_earned
        request.session['activities'].append(farm.__dict__)
    elif request.POST['building'] == 'cave':
        cave = Cave()
        request.session['gold'] += cave.gold_earned
        request.session['activities'].append(cave.__dict__)
    elif request.POST['building'] == 'house':
        house = House()
        request.session['gold'] += house.gold_earned
        request.session['activities'].append(house.__dict__)
    elif request.POST['building'] == 'casino':
        casino = Casino()
        request.session['gold'] += casino.gold_earned
        request.session['activities'].append(casino.__dict__)

    return redirect("/")
