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
