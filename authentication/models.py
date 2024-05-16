from django.db import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# User Model
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Item Model
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Booking Model
class Booking(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

# Feedback Model
class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




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
