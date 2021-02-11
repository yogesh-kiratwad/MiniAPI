from django.contrib import admin
from .models import ProductModel,Cart, FBrand, FCategory

# Register your models here.
@admin.register(FBrand)
class AdminFBrand(admin.ModelAdmin):
    list_display = ['id','fbrand']

@admin.register(FCategory)
class AdminFCategory(admin.ModelAdmin):
    list_display = ['id','fcategory']

@admin.register(ProductModel)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','brand','category']

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['id','brand','category']
    