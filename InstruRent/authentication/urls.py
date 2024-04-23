# authentication/urls.py

from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('signup/', register, name='signup'),
    # You can add more authentication related URLs here
]
