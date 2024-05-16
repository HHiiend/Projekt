from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking, User, Item, CustomUser, Feedback


admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Item)
admin.site.register(CustomUser)
admin.site.register(Feedback)
