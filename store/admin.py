from django.contrib import admin
from .models import Product, Order


# =========================
# Customize Admin Header
# =========================
admin.site.site_header = "Partha Grocery Administration"
admin.site.site_title = "Partha Grocery Admin Portal"
admin.site.index_title = "Welcome to Partha Grocery Control Panel"


# =========================
# Product Admin Customization
# =========================
class ProductAdmin(admin.ModelAdmin):
    # Columns to show in admin list
    list_display = ('id', 'name', 'price', 'stock')

    # Add search box
    search_fields = ('name',)

    # Add filters
    list_filter = ('price', 'stock')

    # Items per page
    list_per_page = 10


# =========================
# Order Admin Customization
# =========================
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'product', 'quantity')
    search_fields = ('customer_name',)
    list_per_page = 10


# Register models with customization
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)