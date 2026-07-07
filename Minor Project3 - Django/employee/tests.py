from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee

class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.employee1 = Employee.objects.create(
            name="Rahul Sharma",
            email="rahul@gmail.com",
            phone="9876543210",
            department="Software Development",
            designation="Python Developer",
            salary=65000.0,
            city="Hyderabad"
        )
        self.employee2 = Employee.objects.create(
            name="Priya Reddy",
            email="priya@gmail.com",
            phone="9123456789",
            department="Human Resources",
            designation="HR Executive",
            salary=45000.0,
            city="Bangalore"
        )

    def test_create_employee(self):
        url = reverse('add_employee')
        data = {
            "name": "Arjun Kumar",
            "email": "arjun@gmail.com",
            "phone": "9988776655",
            "department": "Testing",
            "designation": "QA Engineer",
            "salary": 55000,
            "city": "Chennai"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Employee Added Successfully")
        self.assertEqual(response.data["employee"]["name"], "Arjun Kumar")
        self.assertEqual(Employee.objects.count(), 3)

    def test_view_all_employees(self):
        url = reverse('view_employees')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Rahul Sharma")
        self.assertEqual(response.data[1]["name"], "Priya Reddy")

    def test_update_employee(self):
        url = reverse('update_employee', kwargs={'id': self.employee2.id})
        data = {
            "name": "Priya Reddy",
            "email": "priya.reddy@gmail.com",
            "phone": "9123456789",
            "department": "Human Resources",
            "designation": "Senior HR Executive",
            "salary": 55000,
            "city": "Hyderabad"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Employee Updated Successfully")
        self.assertEqual(response.data["employee"]["email"], "priya.reddy@gmail.com")
        self.assertEqual(response.data["employee"]["designation"], "Senior HR Executive")
        self.assertEqual(response.data["employee"]["salary"], 55000.0)
        self.assertEqual(response.data["employee"]["city"], "Hyderabad")

    def test_delete_employee(self):
        url = reverse('delete_employee', kwargs={'id': self.employee2.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Employee Deleted Successfully")
        self.assertEqual(Employee.objects.count(), 1)

