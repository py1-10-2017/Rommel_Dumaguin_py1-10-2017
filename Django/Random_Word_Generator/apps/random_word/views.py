# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    # response = "placeholder to display index.html
    request.session['random_word'] = get_random_string(length=14)
    print request.session['random_word'].upper()
    if 'random_word_count' not in request.session:
        request.session['random_word_count'] = 0
    else:
        request.session['random_word_count'] += 1
    return render (request, 'random_word/index.html')

def reset(request):
    request.session['random_word_count'] = 0
    return redirect ("/")
