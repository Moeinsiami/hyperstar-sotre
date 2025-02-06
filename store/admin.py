from django.contrib import admin
from .models import Image, Product


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_text', 'title', 'caption')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
