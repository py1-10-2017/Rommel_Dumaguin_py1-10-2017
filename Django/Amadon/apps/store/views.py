# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from products import items # importing list of item objects from products.py

# Create your views here.
# the index function is called when root is visited
def index(request):
    context = {
        "items": items # imported from products.py
    }
    # response = "Hello, I am your first request!"
    return render (request, 'store/index.html', context)
    # return HttpResponse(response)

def process(request, item_id):
    response = "process!"
    if request.method == "POST":
        print "*"*50
        print request.POST
        # print request.POST['name']
        print request.POST['quantity']
        print "*"*50
        try:
            request.session['total_items_count']
        except:
            request.session['total_items_count'] = 0
        try:
            request.session['order_total']
        except:
            request.session['order_total'] = 0
        for item in items:
            # print type(item_id)
            # print item['id']
            # print int(item_id)
            if item['id'] == int(item_id):
                request.session['last_transaction'] = item['price'] * float(request.POST['quantity'])
                request.session['order_total'] += request.session['last_transaction']
                request.session['total_items_count'] += int(request.POST['quantity']) # multiplies price by quantity
                break
        # The reason we have a method to handle POST/session and another method to handle the view file is because it makes reading your code much easier.
        # Also, if the same URL handled both POST and the rendering of the view when you reload that page, it would resubmit the form data. This is not good and is often a common mistake made by a rookie developer.
        # return render (request, 'store/result.html') # REFRESHING THIS PAGE RESUBMITS!
        return redirect ('/result')
    else:
        return render (request, 'store/index.html')
    # return HttpResponse(response)

def result(request):
    # response = "result!"
    return render (request, 'store/result.html')

def logoff(request):
    # response = "logoff!"
    request.session.clear() # start with a clean slate for testing
    return redirect ('/')
