# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error # An action was not successful or some other failure occurred
from .models import User

# Create your views here.
# the index function is called when root is visited
def index(request):
    context = {
        'users': User.objects.all(), # .order_by("key") isn't necessary in this case
    }
    return render (request, 'semi_restful_users/index.html', context)

# USERS
def new(request):
    return render(request, 'semi_restful_users/create.html')

def create(request):
    errors = User.objects.validate(request.POST) # User's objects property (instance of UserManager()) has a method 'validate(self, post_data)', which returns 'errors'
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field) # from django.contrib.messages import error (message.tags includes 'error' class by default)
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        return redirect('/semi_restful_users/new')

    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    return redirect('/semi_restful_users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful_users/show.html', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id) # from user_id, we want to get all this user's info
    }
    return render(request, 'semi_restful_users/update.html', context)

def update(request, user_id):
    errors = User.objects.validate(request.POST) # User's objects property (instance of UserManager()) has a method 'validate(self, post_data)', which returns 'errors'
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field) # from django.contrib.messages import error (message.tags includes 'error' class by default)
        return redirect('/semi_restful_users/{}/edit'.format(user_id))

    this_user = User.objects.get(id=user_id)
    this_user.first_name = request.POST['first_name']
    this_user.last_name = request.POST['last_name']
    # this_user.email = request.POST['email'] # generally we don't ever want to update email
    this_user.save()
    return redirect('/semi_restful_users/{}'.format(user_id)) # redirect to show.html
    # return redirect('/semi_restful_users')

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/semi_restful_users')
