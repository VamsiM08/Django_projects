from django.test import TestCase, Client
from django.urls import reverse

class FacultyViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_faculty_homepage_html(self):
        """Test faculty homepage renders HTML by default"""
        response = self.client.get('/faculty/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Faculty Home Page")
        self.assertTemplateUsed(response, 'faculty/faculty_home.html')

    def test_faculty_homepage_json(self):
        """Test faculty homepage returns JSON with format=json query parameter"""
        response = self.client.get('/faculty/', {'format': 'json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to Faculty App"})

    def test_faculty_details(self):
        """Test faculty details page returns JSON response"""
        response = self.client.get('/faculty/details/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Faculty Details Page"})

    def test_faculty_profile(self):
        """Test faculty profile page returns JSON response"""
        response = self.client.get('/faculty/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Faculty Profile Page"})

    def test_faculty_name_dynamic(self):
        """Test dynamic URL returns correct faculty name"""
        response = self.client.get('/faculty/Rahul/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Faculty Name : Rahul")
        
        response2 = self.client.get('/faculty/Suresh/')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.content.decode(), "Faculty Name : Suresh")
