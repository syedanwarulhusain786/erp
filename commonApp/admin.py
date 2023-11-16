from django.contrib import admin
from .models import Material, Product, ProductMaterial, ProductImage, ProductMaterialImage

class ProductMaterialInline(admin.TabularInline):
    model = ProductMaterial
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductMaterialImageInline(admin.TabularInline):
    model = ProductMaterialImage
    extra = 1

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unit_of_measurement')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    inlines = [ProductMaterialInline, ProductImageInline]

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity_per_piece')
    inlines = [ProductMaterialImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

@admin.register(ProductMaterialImage)
class ProductMaterialImageAdmin(admin.ModelAdmin):
    list_display = ('product_material', 'image')
