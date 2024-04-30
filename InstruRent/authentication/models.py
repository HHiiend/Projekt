from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
# authentication/models.py

from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Override the username field to not be required and unique.
    username = models.CharField(_('username'), max_length=150, unique=False, blank=True)
    email = models.EmailField(_('email address'), unique=True)  # Ensure email is unique
    # Adding a new field for theme settings
    theme_settings = models.CharField(max_length=100, default='default_theme', blank=True)


    USERNAME_FIELD = 'email'    # Use email as the unique identifier
    REQUIRED_FIELDS = []        # Remove email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
