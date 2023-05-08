from django.contrib import admin
from .models import Product , ProductImages , Brand , ProductReview

# Register your models here.
class ProductImagesInLine(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inline = [ProductImagesInLine]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(ProductReview)