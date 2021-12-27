from django.contrib import admin

from hydra_shop.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name', 'price']
    raw_id_fields = ['category']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['product']
    search_fields = ['product']
