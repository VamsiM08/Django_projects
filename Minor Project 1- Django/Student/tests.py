from django.test import TestCase, Client
from django.urls import reverse

class StudentViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_redirect(self):
        """Test root URL redirects to student homepage"""
        response = self.client.get('/')
        self.assertRedirects(response, '/student/')

    def test_student_homepage_html(self):
        """Test student homepage renders HTML by default"""
        response = self.client.get('/student/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student Home Page")
        self.assertTemplateUsed(response, 'student/student_home.html')

    def test_student_homepage_json(self):
        """Test student homepage returns JSON with format=json query parameter"""
        response = self.client.get('/student/', {'format': 'json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to Student App"})

    def test_student_details(self):
        """Test student details page returns JSON response"""
        response = self.client.get('/student/details/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Student Details Page"})

    def test_student_profile(self):
        """Test student profile page returns JSON response"""
        response = self.client.get('/student/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Student Profile Page"})

    def test_student_id_dynamic(self):
        """Test dynamic URL returns correct student ID"""
        response = self.client.get('/student/101/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Student ID : 101")
        
        response2 = self.client.get('/student/999/')
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.content.decode(), "Student ID : 999")
