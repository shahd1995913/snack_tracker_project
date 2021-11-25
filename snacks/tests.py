
from django.urls import reverse
# Create your tests here.
from django.http import response

from django.test import TestCase,SimpleTestCase




class HomeTests(SimpleTestCase):

    def test_code(self):

        url = reverse("snacks")

        response=self.client.get(url)

        self.assertEqual(response.status_code,200)

    def test_templet(self):

        url = reverse("home")

        response=self.client.get(url)

        self.assertTemplateUsed(response,"snacks_list.html")

        self.assertTemplateUsed(response, 'base.html')