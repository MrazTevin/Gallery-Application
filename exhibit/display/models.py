from django.db import models

# Create your models here.

# Location model to enable us choose location

# renaming class Location to Places due to error in terminal;
# django.db.utils.ProgrammingError: relation "display_location" already exists


class Places(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_places(self):
        self.save()

    def delete_places(self):
        self.save()


# iterable tuple to use as choices of category field
# renaming class Category to Order due to error in terminal;
# django.db.utils.ProgrammingError: relation "display_category" already exists


ORDER_CHOICES = (
    ('1', 'Vegetation'),
    ('2', 'Trees'),
    ('3', 'Nature'),
    ('4', 'Abstract'),
    ('5', 'IT & Computers'),
    ('6', 'Animals'),
    ('7', 'Illustrations'),
    ('8', 'Arts'),
    ('9', 'Business'),
    ('10', 'Industries'),
    ('11', 'Objects'),
    ('12', 'Technology'),
    ('13', 'People'),
    ('14', 'Travel'),
)


class Order(models.Model):
    name = models.CharField(max_length=30)
    category_choices = models.CharField(max_length=1, choices=ORDER_CHOICES)

    def __str__(self):
        return self.name

    def save_order(self):
        self.save()

    def delete_order(self):
        self.save()


# renaming class Images to Photos due to error in terminal;
# django.db.utils.ProgrammingError: relation "display_images" already exists


class Photos(models.Model):
    photo_name = models.CharField(max_length=20)
    photo_description = models.CharField(max_length=30)
    # post will contain the image content
    # one location may describe many images while many images may have one
    # location
    places = models.ForeignKey(Places)
    order = models.ForeignKey(Order)

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.photo_name

    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()

    class Meta:
        ordering = ['photo_name']
