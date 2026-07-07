import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_inventory_project.settings')
django.setup()

from inventory.models import Product

# Clear existing products to ensure clean insertion
Product.objects.all().delete()

test_products = [
    {
        "product_name": "Wireless Mouse",
        "category": "Electronics",
        "brand": "Logitech",
        "price": 899,
        "quantity": 50,
        "supplier": "ABC Distributors"
    },
    {
        "product_name": "Mechanical Keyboard",
        "category": "Electronics",
        "brand": "Redragon",
        "price": 2499,
        "quantity": 20,
        "supplier": "XYZ Suppliers"
    },
    {
        "product_name": "USB-C Charger",
        "category": "Accessories",
        "brand": "Samsung",
        "price": 1499,
        "quantity": 35,
        "supplier": "Tech World"
    },
    {
        "product_name": "Gaming Headset",
        "category": "Electronics",
        "brand": "HyperX",
        "price": 3999,
        "quantity": 15,
        "supplier": "Gaming Store"
    },
    {
        "product_name": "External Hard Disk",
        "category": "Storage",
        "brand": "Seagate",
        "price": 5499,
        "quantity": 10,
        "supplier": "Digital Hub"
    }
]

for p_data in test_products:
    product = Product.objects.create(**p_data)
    print(f"Created Product: {product.product_name} (ID: {product.id})")

print("Database populated successfully!")
