# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    # context = {
    #     "key": datetime.now()
    # }
    # response = "Hello, I am your first request!"
    return render (request, 'surveys/index.html')
    # return HttpResponse(response)

def process(request):
    # response = "process!"
    if request.method == "POST":
        print "*"*50
        print request.POST
        # print request.POST['name']
        request.session['test'] = "request.session['test'] = 'test'"
            # python manage.py makemigrations
            # python manage.py migrate
        print request.session['test']
        del request.session['test']
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
        print "*"*50
        response = "processed!"
        if 'submit_count' not in request.session: # Use Try Else next time!
            request.session['submit_count'] = 1
        else:
            request.session['submit_count'] += 1
        return redirect ('/result')
        # The reason we have a method to handle POST/session and another method to handle the view file is because it makes reading your code much easier.
        # Also, if the same URL handled both POST and the rendering of the view when you reload that page, it would resubmit the form data. This is not good and is often a common mistake made by a rookie developer.
    else:
        return render (request, 'surveys/index.html')
    # errors = []
    # validation checks - not required for this assignment
    return HttpResponse(response)

def result(request):
    response = "result!"
    return render (request, 'surveys/result.html')

def logoff(request):
    response = "logoff!"
    request.session.clear() # start with a clean slate for testing
    return render (request, 'surveys/index.html')
