from django.contrib import admin
from .models import Product, Offer, Payment  # importing models module from current folder


admin.site.register(Product) # We want to manage Product in the admin area
admin.site.register(Offer)  # We want to manage Offer in the admin area(object.attribute.method(call))
admin.site.register(Payment)