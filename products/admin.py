
from django.contrib import admin
from .models import (Product)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_pice','description','created_time',
                    'category','product_image']

