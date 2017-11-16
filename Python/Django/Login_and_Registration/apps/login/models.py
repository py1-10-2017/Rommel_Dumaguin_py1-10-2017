# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
# No methods in our new manager should ever catch the whole request object with a parameter! (just parts, like request.POST)
class UserManager(models.Manager):

    def validate_login(self, post_data):
        errors = []
        # check if email found in db
        if len(self.filter(email=post_data['email'])) > 0:
            # check if password matches
            user = self.get(email=post_data['email'])
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append("invalid email/password.")
        else:
            errors.append("invalid email/password.")
        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = {}
        # check for empty keys
        for key, value in post_data.iteritems():
            if key != "confirm_password":
                if len(value) < 1:
                    errors[key] = "{} cannot be blank.".format(key.replace("_"," "))
                # check name fields
                if key == "first_name" or key == "last_name":
                    if key not in errors:
                        # check min lengths
                        if len(value) < 2:
                            errors[key] = "{} should be 2 or more characters.".format(key.replace("_"," "))
                        # check for letters
                        # elif not value.isalpha():
                        elif not re.match(NAME_REGEX, value):
                            errors[key] = "{} should only have letters.".format(key.replace("_"," "))
                if key == "email":
                    if key not in errors:
                        # check for valid email format
                        if not re.match(EMAIL_REGEX, value):
                            errors[key] = "invalid email."
                if key == "password":
                    if key not in errors:
                        # check min length
                        if len(value) < 8:
                            errors[key] = "password must be at least 8 characters"
        if len(errors):
            return errors
        # further validate email and password if inputs are valid
        elif post_data['password'] != post_data['confirm_password']:
            errors['password'] = "passwords didn't match."
            return errors
        # finally check to see if a valid email was submitted (False for /update route)
        # check if email already exists in db
        if len(self.filter(email=post_data['email'])) > 0: # True if matching email found
            errors['email'] = "this email is already registered."
            return errors
        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            # User.objects.create(
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                password=hashed,
            )
            return new_user
        return errors # catch all

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
