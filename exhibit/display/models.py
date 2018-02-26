from django.db import models

# Create your models here.

# Location model to enable us choose location

# renaming class Location to Places due to error in terminal;
# django.db.utils.ProgrammingError: relation "display_location" already exists


class Place(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_place(self):
        self.save()

    def delete_place(self):
        self.save()


# iterable tuple to use as choices of category field
# renaming class Category to Order due to error in terminal;
# django.db.utils.ProgrammingError: relation "display_category" already exists


ORDER_CHOICES = (
    ('11', 'Vegetation'),
    ('12', 'Trees'),
    ('13', 'Nature'),
    ('14', 'Abstract'),
    ('15', 'IT & Computers'),
    ('16', 'Animals'),
    ('17', 'Illustrations'),
    ('18', 'Arts'),
    ('19', 'Business'),
    ('20', 'Industries'),
    ('21', 'Objects'),
    ('22', 'Technology'),
    ('23', 'People'),
    ('24', 'Travel'),
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


class Photo(models.Model):
    photo_name = models.CharField(max_length=20)
    photo_description = models.CharField(max_length=30)
    # post will contain the image content
    # one location may describe many images while many images may have one
    # location
    place = models.ForeignKey(Place)
    order = models.ForeignKey(Order)
    photo = models.ImageField(upload_to='photos/', null="True", blank="True",
                              width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.photo_name

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def search_by_order(cls, search_term):
        display = cls.objects.filter(title__icontains=search_term)
        return display

    @classmethod
    def filter_by_place(cls, place):
        display = cls.objects.filter(place)
        return display

    class Meta:
        ordering = ['photo_name']
