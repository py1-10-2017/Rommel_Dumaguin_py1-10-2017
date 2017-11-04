# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return render (request, 'blogs/index.html')
    # return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        # print request.POST['name']
        request.session['name'] = request.POST['name']
        print request.session['name']
        # print request.POST['desc']
        request.session['desc'] = request.POST['desc']
        print request.session['desc']
        print "*"*50
        return redirect("/")
    else:
    	return redirect("/")
    return redirect('/')

def show(request, number):
    response = "placeholder to display blog " + number # For example /15 should display a message 'placeholder to display blog 15'
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + number
    return HttpResponse(response)

def destroy(request, number):

    return redirect('/')
