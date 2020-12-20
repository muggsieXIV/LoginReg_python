from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['first_name']) < 2:
            errors['first_name'] = "First Name is not long enough. Try again!"
        if len(form_data['last_name']) < 2:
            errors['last_name'] = "Last Name is not long enough. Try again!"
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password is not long enough, try again!"
        if form_data['password'] != form_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match! Try again!"
        return errors 
    
    def login_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email Doesn't look right!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password is not correct, try again!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
