from django.contrib import admin
from .models import Customers, Cases, Products, Contractors
admin.site.register(Customers)
admin.site.register(Cases)
admin.site.register(Products)
admin.site.register(Contractors)