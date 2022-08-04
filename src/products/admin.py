from django.contrib import admin

from .models import Product #relative import

admin.site.register(Product)