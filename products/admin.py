from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'product_date', 'supplier')
    list_display_links=('id', 'title')
    list_filter=('supplier',)
    search_fields=('title','description',)
    list_per_page=25

admin.site.register(Products, ProductsAdmin)