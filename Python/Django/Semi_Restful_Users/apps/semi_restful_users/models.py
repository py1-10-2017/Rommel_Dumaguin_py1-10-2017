# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        # check for empty keys
        for key, value in post_data.iteritems():
            if len(value) < 1:
                errors[key] = "{} cannot be blank!".format(key.replace("_"," "))
            # check name fields
            if key == "first_name" or key == "last_name":
                # check min lengths
                if key not in errors:
                    if len(value) < 2:
                        errors[key] = "{} should be 2 or more characters!".format(key.replace("_"," "))
                    # check if alpha
                    elif not value.isalpha():
                        errors[key] = "{} should only have letters!".format(key.replace("_"," "))

        # check if email was submitted (False for /update route)
        if 'email' in post_data:
            # check for valid email
            if 'email' not in errors and not re.match(EMAIL_REGEX, post_data['email']):
                errors['email'] = "invalid email"
            # then check if email already exists in db
            else:
                if len(self.filter(email=post_data['email'])) > 0: # Returns a matching email from query User.objects.filter(email=post_data['email']))
                    errors['email'] = "email already in use"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        # """
        # models come with a hidden key:
        #     objects = models.Manager()
        # we are going to overwrite this!
        # """
    objects = UserManager()
        # Connect an instance of UserManager to our User model overwriting the old hidden objects key with a new one with extra properties!!!
