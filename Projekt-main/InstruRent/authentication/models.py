from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.Post["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Redirect to a success page
            return redirect("success_url")
        else:
            #Return an "invalid login" error message.abs
            return render(request, "login.html", {"error_message": "Invalid username"})
    else:
        return render(request, "login.html")



# Create your models here.
