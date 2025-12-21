# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(rq):
    return HttpResponse(loader.get_template('index.html').render())