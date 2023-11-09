from django.contrib import admin
from.models import Products
from.models import Categories

class ProdutsAdmin(admin.ModelAdmin):
    list_display=['name', 'price','in_stock'] 
    list_filter=['in_stock']
    #list_editable = ['size']
    search_fields = ['name']

  
admin.site.register(Products, ProdutsAdmin)
admin.site.register(Categories)

# Register your models here.

