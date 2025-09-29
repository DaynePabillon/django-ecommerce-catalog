from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'created_at']
    list_filter = ['created_at', 'price']
    search_fields = ['name', 'description']
    ordering = ['name']
