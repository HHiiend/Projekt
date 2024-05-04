from django.db import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


# User Model
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

# Item Model
class Item(models.Model):
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2)

# Rental Transaction Model
class Rental(models.Model):
    item = models.ForeignKey(Item, related_name='rentals', on_delete=models.CASCADE)
    renter = models.ForeignKey(User, related_name='rentals', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100)



class CustomUser(AbstractUser):
    # Override the username field to not be required and unique.
    username = models.CharField(_('username'), max_length=150, unique=False, blank=True)
    email = models.EmailField(_('email address'), unique=True)  # Ensure email is unique

    USERNAME_FIELD = 'email'    # Use email as the unique identifier
    REQUIRED_FIELDS = []        # Remove email from REQUIRED_FIELDS

    def __str__(self):
        return self.email

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
