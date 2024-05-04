from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, User, Item, Rental


admin.site.register(User)
admin.site.register(CustomUser)
admin.site.register(Item)
admin.site.register(Rental)
