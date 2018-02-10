# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        # check for empty keys
        for key, value in post_data.iteritems():
            if len(value) < 1:
                errors[key] = "{} cannot be blank!".format(key.replace("_"," "))
            # check min lengths
            if key == "name" and key not in errors:
                if len(value) < 5:
                    errors[key] = "{} should be 5 or more characters!".format(key.replace("_"," "))
            if key == "description" and key not in errors:
                if len(value) < 15:
                    errors[key] = "{} should be 15 or more characters!".format(key.replace("_"," "))
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
