from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# this page holds all other       pages


def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
