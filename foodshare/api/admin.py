from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(User)
admin.site.register(FoodListing)
admin.site.register(Review)


