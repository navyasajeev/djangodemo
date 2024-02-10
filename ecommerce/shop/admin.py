from django.contrib import admin

from shop.models import Category,Product
from django.http import HttpResponse
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)