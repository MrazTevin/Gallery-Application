from django.test import TestCase
from .models import Places, Order, Photos

# Create your tests here.


class PlacesTestClass(TestCase):
    # setup method
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
        self.assertTrue(places)


class OrderTestClass(TestCase):
    def setUp(self):
        self.Home = Order(order_choices='Home')

# Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Home, Order))

# Testing method
