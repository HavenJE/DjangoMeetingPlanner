from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# view is a django component that handles a request for a web page.

# create a welcome view page by making a welcome function


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

# create a date function that returns the time of the GET http request


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


# create an about page that talks about yourself 
def about(request):
    return HttpResponse("My name is Haven and I'm an IT graduate!")