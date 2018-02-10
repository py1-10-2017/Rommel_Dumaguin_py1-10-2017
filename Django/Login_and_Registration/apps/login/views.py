# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.messages import error
from django.contrib import messages # we want 'success' as well
from .models import User

# Create your views here.
# the index function is called when root is visited
def index(request):
    context = {
        'users': User.objects.all(), # .order_by("key") isn't necessary in this case
    }
    return render (request, 'login/index.html', context)

def login(request):
    result = User.objects.validate_login(request.POST) # User.objects is set as an instance of UserManager()
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        request.session.clear()
        request.session['login_email'] = request.POST['email']
        return redirect ('/')
    else:
        # request object shouldn't touch the innerworkings of our model
        request.session['user_id'] = result.id # passing user info to success.html
        messages.success(request, "Successfully logged in!")
        return redirect ('/success')

def register(request):
    result = User.objects.validate_registration(request.POST) # User's objects property (instance of UserManager()) has a method 'validate(self, post_data)', which returns 'errors' or 'new_user'
    # if len(result): # can't do this because "object of type 'User' has no len()"
    if type(result) == dict: # if there are errors
        for err, message in result.iteritems():
            messages.error(request, message, extra_tags=err)
        request.session.clear()
        request.session['registration_first_name'] = request.POST['first_name']
        request.session['registration_last_name'] = request.POST['last_name']
        request.session['registration_email'] = request.POST['email']
        return redirect ('/')
    # new_user created and passed from manager into 'result'
    else:
        # request object shouldn't touch the innerworkings of our model
        request.session['user_id'] = result.id # passing user info to success.html
        messages.success(request, "Successfully registered!")
        return redirect ('/success')

def success(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    request.session.clear()
    return render (request, 'login/success.html', context)

def logoff(request):
    return redirect ('/')

def delete(request): # For testing purposes
    User.objects.last().delete()
    return redirect ('/')
