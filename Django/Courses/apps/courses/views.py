# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error # An action was not successful or some other failure occurred
from .models import Course

# Create your views here.
# the index function is called when root is visited
def index(request):
    context = {
        'courses': Course.objects.all(), # .order_by("key") isn't necessary in this case
    }
    return render (request, 'courses/index.html', context)

def create(request):
    print request.POST
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        request.session['name'] = request.POST['name']
        request.session['description'] = request.POST['description']
        return redirect('/courses')

    Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
    )
    return redirect('/courses')

def confirm_destroy(request, course_id):
    context = {
        'this_course': Course.objects.get(id=course_id)
    }
    return render (request, 'courses/remove.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')
