from django.db import models

# Create your models here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255,primary_key=True)
    username = models.CharField(max_length=255)
    email_add = models.EmailField()
    password = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='media/')



model = User
fields = (
    'email',
    'first_name',
    'last_name'
)