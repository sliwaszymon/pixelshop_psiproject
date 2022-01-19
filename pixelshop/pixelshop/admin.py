"""Admin file."""

# Django
from django.contrib import admin

# Project
from pixelshop.models import Order
from pixelshop.models import PixelArt
from pixelshop.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(PixelArt)
