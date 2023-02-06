from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/djangoapp')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/djangoapp/login')
    else:
        return render(request, 'login.html')


def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'index.html', context)

def aboutus(request):
   return render(request, 'aboutus.html') 

def contactus(request):
   return render(request, 'contactus.html') 


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            print('username taken')
            messages.info(request,'Username already exists')
            return redirect('/djangoapp/signup')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
        return redirect('/djangoapp')
    else:
        return render(request, 'signup.html') 

def logout(request):
    auth.logout(request)
    return redirect('/djangoapp')
    







# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

