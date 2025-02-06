from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100,null=False,blank=False)
#     def __str__(self):
#         return self.name

# class Listing(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     owner = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=20)
#     description = models.TextField(blank=True)
#     price = models.IntegerField()
#     bedrooms = models.IntegerField()
#     bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
#     garage = models.IntegerField(default=0)
#     sqft = models.IntegerField()
#     lot_size = models.DecimalField(max_digits=5, decimal_places=1)
#     category = models.CharField(choices=CATEGORY_PLACES, max_length=5)
#     photo_main = models.ImageField(upload_to='product')
#     photo_1 = models.ImageField(upload_to='product', blank=True)
#     photo_2 = models.ImageField(upload_to='product', blank=True)
#     photo_3 = models.ImageField(upload_to='product', blank=True)
#     photo_4 = models.ImageField(upload_to='product', blank=True)
#     photo_5 = models.ImageField(upload_to='product', blank=True)
#     photo_6 = models.ImageField(upload_to='product', blank=True)
#     is_published = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    
    def __str__(self):
        return self.name

class Listing(models.Model):
    CATEGORY_PLACES = (
    ('DAY','Dayton'),
    ('CNG','Cincinnati'),
    ('CMH','Columbus'),
    ('MCE','Mason'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    owner_photo = models.ImageField(upload_to='product', blank=True)
    owner_number = models.DecimalField(max_digits=10 ,decimal_places=0,default=0)
    owner_email = models.CharField(max_length=200,null=True,blank=True)
    year_built = models.IntegerField(default=0)
    school_district = models.BooleanField(default=True)
    commute = models.BooleanField(default=True)
    pet_friendly = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=6, decimal_places=1)
    city = models.CharField(choices=CATEGORY_PLACES, max_length=10,default='DAY')
    photo_main = models.ImageField(upload_to='product')
    photo_1 = models.ImageField(upload_to='product', blank=True)
    photo_2 = models.ImageField(upload_to='product', blank=True)
    photo_3 = models.ImageField(upload_to='product', blank=True)
    photo_4 = models.ImageField(upload_to='product', blank=True)
    photo_5 = models.ImageField(upload_to='product', blank=True)
    photo_6 = models.ImageField(upload_to='product', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

   
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class BookAppointment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(default=now,null=True, blank=True)
    agree_termsConditions = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.listing.title},{self.customer.name}"
    
class WishListItem(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)