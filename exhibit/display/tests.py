from django.test import TestCase
from .models import Places, Order, Photos

# Create your tests here.

# setup method


class PlacesTestClass(TestCase):
    def setUp(self):
        self.outdoor = Places(name='outdoor')


# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.outdoor, Places))

# Testing method
    def test_save_method(self):
        self.outdoor.save_places()
        places = Places.objects.all()
        self.assertTrue(places)

    def test_delete_method(self):
        self.outdoor = Places(name='outdoor')
        self.outdoor.save_places()
        self.outdoor.delete_places()
        places = Places.objects.all()
