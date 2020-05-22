from django.contrib import admin

from .models import Supplier

class SuppliersAdmin(admin.ModelAdmin):
    list_display=('id', 'company_name',  'address')
    list_display_links=('id', 'company_name')
    list_filter=('company_name','city', 'address')
    search_fields=('company_name','description',)
    list_per_page=25

admin.site.register(Supplier,SuppliersAdmin)
