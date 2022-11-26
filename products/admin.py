from django.contrib import admin
from .models import Product,ProductImages,ProductReviews,Brand,Category
# Register your models here.


class ProductImagesTabular(admin.TabularInline):
    model=ProductImages
    


class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImagesTabular]
    list_display=['name','flag','quantity','price']
    list_filter=['flag','brand','category','price']
    search_fields=['name','desc','subtitle']

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReviews)
admin.site.register(Brand)
admin.site.register(Category)