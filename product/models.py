from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 
from django.utils.translation import gettext as _ 
from django.utils.text import slugify

# Create your models here.

FLAG_TYPES = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale')
)

class Product (models.Model) : 
    name = models.CharField(_('name'),max_length=120)
    image = models.ImageField(_('image'),upload_to='products')
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    subtitle = models.CharField(_('subtitle'),max_length=300)
    description = models.TextField(_('description'),max_length=20000)
    flag = models.CharField(_('flag'),max_length=10,choices=FLAG_TYPES)
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True,unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) 



class ProductImages (models.Model): 
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')

    def __str__(self):
        return str(self.product)
    

class Brand (models.Model):
    name = models.CharField(_('name'),max_length=100)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(null=True,blank=True,unique=True)

    def __str__(self):
        return self.name


class ProductReview (models.Model):
    user = models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    rate = models.IntegerField(_('rate'))
    review = models.TextField(_('review'),max_length=400)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return str(self.user) 

