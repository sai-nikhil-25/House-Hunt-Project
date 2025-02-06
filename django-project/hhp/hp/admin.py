from django.contrib import admin
from . models import Category, Customer, Listing,BookAppointment, WishListItem

# Register your models here.
@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Listing)
class ListingModelAdmin(admin.ModelAdmin):
    list_display = ['owner','title','address','city','state','zipcode','description','price','bedrooms','bathrooms','garage','sqft','lot_size','category','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_published']

@admin.register(Customer)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','name','city','mobile','zipcode','state']

@admin.register(BookAppointment)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('listing', 'customer', 'appointment_date','agree_termsConditions')
    list_filter = ('listing', 'appointment_date')
    search_fields = ('listing__title', 'customer__name', 'customer__email')

@admin.register(WishListItem)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ('listing','customer')