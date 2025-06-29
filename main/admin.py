from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProducrAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available',
                     'created', 'update']
    list_filter = ['available', 'created', 'update', 'category']
    list_editable = ['price', 'available']  
    prepopulated_fields = {'slug': ('name', )}



