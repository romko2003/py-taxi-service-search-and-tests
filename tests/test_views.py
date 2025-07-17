from django.test import TestCase
from django.urls import reverse
from taxi.models import Driver, Car, Manufacturer


class SearchTests(TestCase):
    def setUp(self):
        self.driver1 = Driver.objects.create_user(username="johnny",
                                                  password="pass",
                                                  license_number="ABC12345")
        self.driver2 = Driver.objects.create_user(username="sarah",
                                                  password="pass",
                                                  license_number="XYZ67890")

        self.car1 = Car.objects.create(model="Tesla X",
                                       brand="Tesla")
        self.car2 = Car.objects.create(model="Toyota Corolla",
                                       brand="Toyota")

        self.manufacturer1 = \
            (Manufacturer.objects.create(name="Tesla",
                                         country="USA"))
        self.manufacturer2 = \
            (Manufacturer.objects.create(name="Toyota", country="Japan"))

    def test_driver_search(self):
        response = (self.client.get(reverse("taxi:driver-list"),
                                    {"username": "john"}))
        self.assertContains(response, "johnny")
        self.assertNotContains(response, "sarah")

    def test_car_search(self):
        response = self.client.get(reverse("taxi:car-list"),
                                   {"model": "Tesla"})
        self.assertContains(response, "Tesla X")
        self.assertNotContains(response, "Toyota Corolla")

    def test_manufacturer_search(self):
        response = self.client.get(reverse("taxi:manufacturer-list"),
                                   {"name": "Toyota"})
        self.assertContains(response, "Toyota")
        self.assertNotContains(response, "Tesla")
