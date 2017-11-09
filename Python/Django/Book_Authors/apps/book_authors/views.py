# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
# from module_name import list_name # importing list of objects from module_name.py

# Create your views here.
# the index function is called when root is visited
def index(request):
    # context = {
    #     "key": datetime.now(),
    #     "list_name": list_name # imported from module_name.py
    # }
    response = "Hello, I am your first request!"
    # return render (request, 'app_name/index.html', context)
    # return render (request, 'app_name/index.html')
    return HttpResponse(response)
