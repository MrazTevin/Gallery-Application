from django.test import TestCase
from .models import Place, Order, Photo

# Create your tests here.


class PlaceTestClass(TestCase):
    # setup method
    def setUp(self):
        self.outdoor = Place(name='outdoor')


# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.outdoor, Place))

# Testing method
    def test_save_method(self):
        self.outdoor.save_place()
        place = Place.objects.all()
        self.assertTrue(place)

    def test_delete_method(self):
        self.outdoor = Place(name='outdoor')
        self.outdoor.save_place()
        self.outdoor.delete_place()
        place = Place.objects.all()
        self.assertTrue(place)


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


class PhotoTestClass(TestCase):
    # setup method
    def setUp(self):

        # creating a new place and saving it
        self.outdoor = Place(name='outdoor')
        self.outdoor.save_place()

        # creating a new order and saving it
        self.new_Home = Order(name='Home')
        self.new_Home.save()

        self.new_photo = Photo(
            photo_name='Macbook', photo_description='macbook pro on a table')
        self.new_photo.save()

        self.new_photo.place.add(self.new_place)
        self.new_photo.order.add(self.new_place)

    # Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Macbook, Photo))

    def tearDown(self):
        Place.objects.all().delete()
        Order.objects.all().delete()
        Photo.objects.all().delete()


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
