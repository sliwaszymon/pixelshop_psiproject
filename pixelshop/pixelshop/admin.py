from django.contrib import admin
from pixelshop.models import User, Order, PixelArt

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(PixelArt)
