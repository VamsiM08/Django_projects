from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

# Create your tests here.

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create initial products for testing
        self.product1 = Product.objects.create(
            product_name="Wireless Mouse",
            category="Electronics",
            brand="Logitech",
            price=899,
            quantity=50,
            supplier="ABC Distributors"
        )
        self.product2 = Product.objects.create(
            product_name="Mechanical Keyboard",
            category="Electronics",
            brand="Redragon",
            price=2499,
            quantity=20,
            supplier="XYZ Suppliers"
        )

    def test_view_all_products(self):
        url = reverse('view_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['product_name'], "Wireless Mouse")
        self.assertEqual(response.data[1]['product_name'], "Mechanical Keyboard")

    def test_add_new_product_success(self):
        url = reverse('add_product')
        data = {
            "product_name": "USB-C Charger",
            "category": "Accessories",
            "brand": "Samsung",
            "price": 1499,
            "quantity": 35,
            "supplier": "Tech World"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Product Added Successfully")
        self.assertIn('product', response.data)
        self.assertEqual(response.data['product']['product_name'], "USB-C Charger")
        self.assertEqual(response.data['product']['price'], 1499)
        self.assertTrue(Product.objects.filter(product_name="USB-C Charger").exists())

    def test_add_new_product_invalid_data(self):
        url = reverse('add_product')
        # Missing product_name
        data = {
            "category": "Accessories",
            "brand": "Samsung",
            "price": 1499,
            "quantity": 35,
            "supplier": "Tech World"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product_success(self):
        url = reverse('update_product', kwargs={'pk': self.product1.pk})
        data = {
            "product_name": "Wireless Mouse (Updated)",
            "category": "Electronics",
            "brand": "Logitech",
            "price": 999,
            "quantity": 45,
            "supplier": "ABC Distributors"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Product Updated Successfully")
        self.assertEqual(response.data['product']['product_name'], "Wireless Mouse (Updated)")
        self.assertEqual(response.data['product']['price'], 999)
        self.assertEqual(response.data['product']['quantity'], 45)
        
        # Verify db updated
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.product_name, "Wireless Mouse (Updated)")
        self.assertEqual(self.product1.price, 999)

    def test_update_product_not_found(self):
        url = reverse('update_product', kwargs={'pk': 999})
        data = {
            "product_name": "Not Found",
            "category": "Electronics",
            "brand": "Logitech",
            "price": 999,
            "quantity": 45,
            "supplier": "ABC Distributors"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product_success(self):
        url = reverse('delete_product', kwargs={'pk': self.product1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Product Deleted Successfully")
        self.assertFalse(Product.objects.filter(pk=self.product1.pk).exists())

    def test_delete_product_not_found(self):
        url = reverse('delete_product', kwargs={'pk': 999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
