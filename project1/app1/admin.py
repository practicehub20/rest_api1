from django.contrib import admin
from app1.models import ProductModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['idno', 'name', 'price', 'qty']

