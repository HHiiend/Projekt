# Create your views here.
# authentication/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can also add auto-login or redirect to profile setup here
            return redirect(reverse('login'))  # Redirect to login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
