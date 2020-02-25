from django.contrib import admin

# Register your models here.

from .models import Product #relative import, sind im gleichen Verzeichnis

admin.site.register(Product)