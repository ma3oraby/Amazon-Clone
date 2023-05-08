import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django 
django.setup()

from faker import Faker
import random
from product.models import Product , Brand , ProductImages , ProductReview





def seed_product_images(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    for x in range(n): 
        ProductImages.objects.create(
            product = Product.objects.get(id=random.randint(1,5000)) , 
            image = f"productimages/{images[random.randint(0,12)]}" , 
        )
    print(f'{n} Products Images Seeded')

# seed_brand(100)
#seed_product(500)
seed_product_images(10000)