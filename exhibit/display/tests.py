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
        self.Home = Order(name='Home')

# Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Home, Order))

# Testing method
    def test_save_method(self):
        self.Home.save_order()
        order = Order.objects.all()
        self.assertTrue(order)

    def test_delete_method(self):
        self.Home = Order(name='Home')
        self.Home.save_order()
        self.Home.delete_order()
        order = Order.objects.all()
        self.assertTrue(order)


class PhotosTestClass(TestCase):
    # setup method
    def setUp(self):
        self.Macbook = Photos(
            photo_name='Macbook', photo_description='macbook pro on a table')

    # Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Macbook, Photos))
#
# # Testing method
#
#     def test_save_method(self):
#         self.Macbook.save_photos()
#         photos = Photos.objects.all()
#         self.assertTrue(photos)
#
#     def test_delete_method(self):
#         self.Macbook = Photos(photo_name='Macbook',
#                               photo_description='macbook pro on a table', blank='True')
#         self.Macbook.save_photos()
#         self.macbook.delete_photos()
#         photos = Photos.objects.all()
#         self.assertTrue(photos)
