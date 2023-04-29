from django.contrib import admin
from .models import Product , ProductImages , Brand , ProductReview

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(ProductReview)