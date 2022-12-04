import django
import os
from .products.models import Product,Brand,Category
from faker import Faker
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def seed_categories(n):
    fake=Faker()
    images=['1.png','2.png','3.jpeg','4.jpg','5.png']
    for _ in range(n):
        name=fake.name()
        image=f"category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name=name,
            image=image
        )
        print(f'Succssefully seeded {n} categrories')


def seed_brands(n):
    fake=Faker()
    images=['1.png','2.jpg','3.png','4.png','5.png','6.png','7.jpg','8.jpg','9.png','10.png']
    for _ in range(n):
        name=fake.name()
        image=f"brand/{images[random.randint(0,5)]}"
        Category.objects.create(
            name=name,
            image=image,
            category=Category.objects.get(id=random.randint(1,7))
        )
        print(f'Succssefully seeded {n} brands')



def seed_products(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','7.jpg','8.jpg','9.jpg','10.jpeg','11.jpeg','12.jpg','13.jpg','14.jpeg','15.jpg','16.png']
    for _ in range(n):
        name=fake.name()
        image=f"brand/{images[random.randint(0,5)]}"
        Category.objects.create(
            name=name,
            image=image,
            category=Category.objects.get(id=random.randint(1,7)),
            desc=fake.text(max_nb_chars=10000)

        )

    print(f'Succssefully seeded {n} products')




seed_categories(5)
seed_brands()
seed_products()