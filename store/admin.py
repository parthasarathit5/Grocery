from django.contrib import admin
from .models import Product, Order


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    search_fields = ('name',)


# Order Admin (FIXED)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total', 'created_at')
    search_fields = ('name', 'phone')


# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


# Admin page customization
admin.site.site_header = "Partha Grocery Administration"
admin.site.site_title = "Partha Grocery Admin"
admin.site.index_title = "Welcome to Partha Grocery Control Panel"