from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import VenueForm
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Customer
from .models import *
from .models import Booking
from datetime import datetime
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError
from .models import Review
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Booking, Venue, Customer



def logout_view(request):
    logout(request)
    return redirect('home')

def amenities(request):
    return render(request, 'amenities.html')

def booking_availability(request):
    return render(request, 'booking-availability.html')


def cancellation(request):
    return render(request, 'cancellation.html')

def edit_venue(request):
    return render(request, 'edit_venue.html')

def images(request):
    return render(request, 'images.html')

def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request,'index1.html')

def user_login(request):
    return render(request, 'login.html')

def modifying_details(request):
    return render(request, 'modifying-details.html')

def notification(request):
    return render(request, 'notification.html')

def price(request):
    return render(request, 'price.html')


def register_process(request):
    if request.method == 'POST':
        username = request.POST.get('newUsername')
        password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register-login.html', {'error': 'Username is already taken.'})
            else:
                user = User.objects.create_user(username=username, password=password)
                customer = Customer.objects.create(
                        name= user,
                        email = email,
                        phoneNo = phoneNo,
                        password = password
                    )
                customer_id = customer.pk
                success_message = "Registration successful! Your customer ID is: %s" % customer_id
                messages.success(request, success_message)
                customer.save()
                return redirect('register_login')
        else:
            return render(request, 'register-login.html', {'error': 'Passwords do not match.'})

    return render(request, 'register-login.html')


def login_process(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'register-login.html')


def register_admin(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        phoneNo = request.POST.get('MobileNumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=name).exists():
                return render(request, 'login.html', {'error': 'Username is already taken.'})
            else:
                firstname ="admin"
                user = User.objects.create_user(username=name, password=password)
                admin = Admin.objects.create(
                        name= user,
                        email = email,
                        phoneNo = phoneNo,
                        password = password
                    )
                admin.save()
                return redirect('/login/')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})

    return render(request, 'register.html')

def register_login(request):
    return render(request, 'register-login.html')
    
def register(request):
    return render(request, 'register.html')

def reviews(request):
    return render(request, 'reviews.html')



def view_booking(request):
    return render(request, 'view_booking.html')

def home(request):
    return render(request, 'home.html')



def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, 'Venue added successfully!')
        else:
            messages.error(request, 'Error adding venue. Please try again.')
    else:
        form = VenueForm()
    return render(request, 'add_venue.html', {'form': form})

def all_venues(request):
    venues = Venue.objects.all()
    return render(request, 'all_venues.html', {'venues': venues})  


def search_results(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        venues = Venue.objects.filter(location=location)
        return render(request, 'search_results.html', {'venues': venues})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        admin = authenticate(username=username, password=password)
        if admin is not None:
            if admin.is_staff:
                login(request, admin)
                return redirect('index1')  
            else:
                error = "You are not authorized to access this page."
                return render(request, 'login.html', {'error': error})
        else:
            error = "Invalid username or password."
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def check_availability(selected_date):
    if Booking.objects.filter(date=selected_date).exists():
        return False
    else:
        return True


from django.utils import timezone
def book_venue(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == 'POST':
        selected_date = request.POST.get('date')
        booking_price = request.POST.get('booking-price')
        venue_name = request.POST.get('venue-name')  

        if not selected_date:
            messages.error(request, "Date is required.")
            return redirect('book-venue')

        selected_datetime = timezone.make_aware(datetime.strptime(selected_date, '%Y-%m-%d'))

        if selected_datetime <= timezone.now():
            messages.error(request, "Please select a future date.")
            return redirect('book-venue')

        if Booking.objects.filter(date=selected_datetime).exists():
            messages.error(request, "Venue is already booked for the selected date. Please choose another date.")
            return redirect('book-venue')

        user = request.user

        try:
            customer = Customer.objects.get(name=user)
            venue = Venue.objects.get(venue_name=venue_name)
            booking = Booking.objects.create(
                date=selected_datetime,
                booking_price=booking_price,
                customer=customer,
                venue=venue
            )

            messages.success(request, 'Venue booked successfully!')
            return redirect('book-venue')

        except Customer.DoesNotExist:
            messages.error(request, 'Customer does not exist.')

        except Venue.DoesNotExist:
            messages.error(request, 'Selected venue does not exist.')

        except Exception as e:
            messages.error(request, str(e))

    venues = Venue.objects.all()  
    return render(request, 'book-venue.html', {'venues': venues})



@login_required
def rescheduling(request, booking_id):
    if request.method == 'POST':
        new_date = request.POST.get('new_date')
        booking = Booking.objects.get(pk=booking_id)
        booking.date = new_date
        booking.save()
        return redirect('view_bookings')
    else:
        return render(request, 'rescheduling.html', {'booking_id': booking_id})

@login_required
def your_booking(request):
    try:
        user = request.user
        
        bookings = Booking.objects.filter(customer__name=user)
        
        return render(request, 'your-booking.html', {'bookings': bookings})
            
    except Booking.DoesNotExist:
        message = "You have not made any bookings yet."
        return render(request, 'your-booking.html', {'message': message})


def update_booking(request):
    if request.method == 'POST':
        booking_id = request.POST['booking_id']
        new_date = request.POST['date']

        try:
            booking = Booking.objects.get(booking_id=booking_id)
            if Booking.objects.filter(venue=booking.venue, date=new_date).exclude(booking_id=booking_id).exists():
             
                messages.error(request, "Date is not available. Please choose another date.")
                return redirect('update_booking', booking_id=booking_id)

            booking.date = new_date
            booking.save()

            messages.success(request, "Booking updated successfully!")
            return redirect('your_booking')

        except Booking.DoesNotExist:
            messages.error(request, "Booking not found. Please try again.")
            return redirect('your_booking')

    return redirect('your_booking')  

def cancel_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, pk=booking_id)
        
        booking.delete()
        
        messages.success(request, 'Booking canceled successfully!')
        
        return redirect('your_booking') 
    return render(request, 'your-booking.html')  



def reviews(request):
    if request.method == 'POST':
        reviewer_name = request.POST.get('name')
        review_text = request.POST.get('review-text')
        review = Review.objects.create(reviewer_name=reviewer_name, review_text=review_text)
        return JsonResponse({
            'name': reviewer_name,
            'review_text': review_text,
            'created_at': review.created_at.strftime('%Y-%m-%d') 
        })
    else:
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'reviews': reviews})


def fetch_venue_location(request):
    venues = Venue.objects.all()
    return render(request, 'search_venues.html', {'venues': venues})

def search_venues(request):
    locations = Venue.objects.values_list('location', flat=True).distinct()

    return render(request, 'search-venues.html', {'locations': locations})



def all_venues(request):
    venues = Venue.objects.all()
    return render(request, 'all_venues.html', {'venues': venues})

def edit_venue(request):
    venue_name = request.POST.get('venue_name')
    venue = get_object_or_404(Venue, venue_name=venue_name)
    return render(request, 'edit_venue.html', {'venue': venue})

def update_venue(request):
    if request.method == 'POST':
        print("In update_venue if")
        venue_name = request.POST.get('venue_name')
        try:
            venue = Venue.objects.get(venue_name=venue_name)
        except Venue.DoesNotExist:
            return HttpResponseServerError("Venue with name '{}' does not exist.".format(venue_name))

        venue.location = request.POST.get('location')
        venue.capacity = request.POST.get('capacity')
        venue.amenities = request.POST.get('amenities')
        venue.pricing = request.POST.get('pricing')
        venue.availability = request.POST.get('availability') == 'yes'
        venue.image = request.FILES.get('image')
        venue.save()

        messages.success(request, 'Venue updated successfully!')

        return redirect('all_venues')
    else:
        messages.error(request, 'Error updating venue. Please try again.')
        pass

def fetch_venue_details(request):
    if request.method == 'GET' and 'venue_name' in request.GET:
        venue_name = request.GET.get('venue_name')
        venue = Venue.objects.get(id=venue_name)
        data = {
            'name': venue.venue_name,
            'location': venue.location,
            'capacity': venue.capacity,
            'amenities': venue.amenities,
            'pricing': venue.pricing,
            'availability': venue.availability,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request'})

def view_booking(request):
    bookings = Booking.objects.all()
    return render(request, 'view_booking.html', {'bookings': bookings})

def get_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'get_reviews.html', {'reviews': reviews})

def index1(request):
    venues_with_images = Venue.objects.exclude(image__isnull=True).exclude(image__exact='')
    welcome_message = "Welcome {} ...".format(request.user.username)
    return render(request, 'index1.html', {'venues_with_images': venues_with_images, 'welcome_message': welcome_message})


def index(request):
    venues_with_images = Venue.objects.exclude(image__isnull=True).exclude(image__exact='')
    welcome_message = "Welcome {} ...".format(request.user.username)
    return render(request, 'index.html', {'venues_with_images': venues_with_images, 'welcome_message': welcome_message})
    
def delete_venue(request):
    if request.method == 'POST':
        venue_name = request.POST.get('venue_name')
        try:
            venue = Venue.objects.get(venue_name=venue_name)
            venue.delete()
            messages.success(request, 'Venue deleted successfully!')
        except Venue.DoesNotExist:
            return HttpResponseServerError("Venue with name '{}' does not exist.".format(venue_name))
    else:
        messages.error(request, 'Error deleting venue. Please try again.')
    return redirect('all_venues')