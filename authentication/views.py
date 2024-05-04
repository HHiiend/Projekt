# Create your views here.
# authentication/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from rest_framework import views, status, permissions
from rest_framework.response import Response

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

class UserSettingsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'theme': user.theme_settings})

    def put(self, request):
        user = request.user
        user.theme_settings = request.data.get('theme')
        user.save()
        return Response({'message': 'Settings updated'}, status=status.HTTP_200_OK)