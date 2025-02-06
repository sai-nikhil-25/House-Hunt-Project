from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from . forms import CustomerRegistrationForm,Profile,Appointment
from django.contrib import messages
from .models import BookAppointment, Customer,Category,Listing, WishListItem
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    category = request.GET.get('category')
    if category == None:
       listings = Listing.objects.all()
    else:
        listings = Listing.objects.filter(category__name=category)  

    categories = Category.objects.all()
    context = {'categories':categories,'listings':listings}
    return render(request,"hp/mainPage.html",context)

def placesFilter(request,val):
    if val == None:
         listings = Listing.objects.all()
    else:
        listings = Listing.objects.filter(state=val)

    categories = Category.objects.all()
    context = {'categories': categories, 'listings': listings}
    return render(request, "hp/mainPage.html", context)

# def category(request, category):
#     place = request.GET.get('place') 
#     if place:
#         return redirect('places', val=place)
#     else:
#         category_listings = Listing.objects.filter(category__name=category)
#         categories = Category.objects.all()
#         context = {'categories': categories, 'listings': category_listings}
#         return render(request, "hp/mainPage.html", context)

def category(request,category):
    place = request.GET.get('place')
    category_listings = Listing.objects.filter(category__name=category)
    categories = Category.objects.all()
    selected_place = request.GET.get('place')
    context = {
        'categories': categories,
        'listings': category_listings,
        'selected_place': selected_place  # Pass the selected place to the context
    }
    return render(request, "hp/mainPage.html", context)

def view(request,pk):
    #  listing = Listing.objects.get(pk=pk)
     listing = get_object_or_404(Listing, pk=pk)
     customer = Customer.objects.get(user=request.user)
     viewed_from_view_appointments = request.GET.get('view_appointments', False)
     is_in_wishlist = WishListItem.objects.filter(listing=listing, customer=customer).exists()
     context = {
         'listing':listing,
          'viewed_from_view_appointments': viewed_from_view_appointments,
          'is_in_wishlist': is_in_wishlist,
         }
     return render(request,"hp/viewPage.html",context)

def appointment(request):
    return render(request, "hp/appointmentPage.html")


class RegisterView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'hp/register.html',locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully registered!!!")
        else:
            messages.warning(request,"Invalid details")
        return render(request, 'hp/register.html',locals())

class ProfileView(View):  
    def get(self,request):
        form = Profile()
        return render(request,'hp/profile.html',locals())
    def post(self,request):
        form = Profile(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Profile Saved")
        else:
            messages.warning(request,"Invalid details!")
        return render(request,'hp/profile.html',locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'hp/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = Profile(instance=add)
        return render(request,'hp/updateAddress.html',locals())
        
    def post(self,request,pk):
        form = Profile(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.user = request.user
            add.name = form.cleaned_data['name']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Profile Updated!!")
        else:
            messages.warning(request,"Invalid Details!!")
        return redirect('address')
    
# def book_appointment(request):
#     if request.method == 'POST':
#         form = BookAppointmentForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone_number = form.cleaned_data['phone_number']
#             appointment_date = form.cleaned_data['appointment_date']
#             appointment_time = form.cleaned_data['appointment_time']
#             confirmation = form.cleaned_data['confirmation']
            

#             return redirect('success_page')
#     else:
#         form = BookAppointmentForm()

#     return render(request, 'hp/appointmentPage.html', {'form': form})

def book_appointment(request,listing_pk):
    customer = Customer.objects.get(user=request.user)
    listing = get_object_or_404(Listing,pk=listing_pk)
    if request.method == 'POST':
        form = Appointment(request.POST)
        if form.is_valid():
            # Save the form data to the database
            appointment = form.save(commit=False)
            appointment.customer = customer
            appointment.listing = listing
            appointment.save()
            # form.save()
            # Redirect to a success page or some other URL
            return redirect('success_page')
    else:
        form = Appointment(initial={
            'customer_name': customer.name,
            'customer_phone': customer.mobile,
            'customer_email': customer.user.email,
            'listing_title': listing.title,  
        })
    
    return render(request, 'hp/appointmentPage.html', {'form': form})

def success_page(request):
    return render(request,'hp/success_page.html')

@login_required
def view_appointments(request):
    # appointments = BookAppointment.objects.all()
    customer = Customer.objects.get(user=request.user)
    appointments = BookAppointment.objects.filter(customer=customer)
    return render(request,'hp/view_appointments.html',{'appointments':appointments})

def toggle_wishlist(request,listing_pk):
    customer = Customer.objects.get(user=request.user)
    wishlist_item, created = WishListItem.objects.get_or_create(listing_id=listing_pk,customer = customer)

    if not created:
        wishlist_item.delete()
    return redirect('viewPage', pk=listing_pk)


def wishlist(request):
    customer = Customer.objects.get(user=request.user)
    wishlist_items = WishListItem.objects.filter(customer=customer)
    return render(request, 'hp/wishlist.html', {'wishlist_items': wishlist_items})

def aboutus(request):
    return render(request,'hp/aboutus.html')

def contactus(request):
    return render(request,'hp/contactus.html')