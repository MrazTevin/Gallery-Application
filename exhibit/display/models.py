from django.db import models

# Create your models here.

# Location model to enable us choose location


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# iterable tuple to use as choices of category field
CATEGORY_CHOICES = (
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


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_choices = models.CharField(max_length=1, choices=CATEGORY_CHOICES)


class Images(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    # post will contain the image content
    # one location may describe many images while many images may have one
    # location
    location = models.ForeignKey(Location, blank=True, default=True)
    category = models.ForeignKey(Category, blank=True, default=True)

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']
