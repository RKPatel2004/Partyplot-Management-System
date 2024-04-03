from django.conf.urls import url
from django.contrib import admin
from .views import add_venue
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'), 
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^logout/', views.logout_view, name='logout'), 
    url(r'^index/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^register-login/', views.register_login, name='register_login'),
    url(r'^search-venues/', views.search_venues, name='search_venues'),
    url(r'^book-venue/', views.book_venue, name='book_venue'),
    url(r'^booking-availability/', views.booking_availability, name='booking_availability'),
    url(r'^cancellation/', views.cancellation, name='cancellation'),
    url(r'^images/', views.images, name='images'),
    url(r'^price/', views.price, name='price'),
    url(r'^reviews/', views.reviews, name='reviews'),
    url(r'^amenities/', views.amenities, name='amenities'),  
    url(r'^edit_venue/', views.edit_venue, name='edit_venue'),
    url(r'^notification/', views.notification, name='notification'),  
    url(r'^view_booking/', views.view_booking, name='view_booking'), 
    url(r'^modifying-details/', views.modifying_details, name='modifying_details'),  
    url(r'^register_process/', views.register_process, name='register_process'), 
    url(r'^login_process/', views.login_process, name='login_process'),
    url(r'^add_venue.html/', views.add_venue, name='add_venue'),
    url(r'search_results/', views.search_results, name='search_results'),
    url(r'register_admin/', views.register_admin, name='register_admin'),
    url(r'check-availability/', views.check_availability, name='check-availability'),  
    url(r'book-venue/', views.book_venue, name='book-venue'), 
    url(r'rescheduling/', views.rescheduling, name='rescheduling'),
    url(r'^your-booking/', views.your_booking, name='your_booking'),
    url(r'^cancel-booking/', views.cancel_booking, name='cancel_booking'),
    url(r'^reviews/', views.reviews, name='reviews'), 
    url(r'^update_booking/', views.update_booking, name='update_booking'),
    url(r'^search-venues/', views.fetch_venue_location, name='fetch_venue_location'),
    url(r'^edit_venue/', views.edit_venue, name='edit_venue'),
    url(r'^update_venue/', views.update_venue, name='update_venue'),
    url(r'^all-venues/', views.all_venues, name='all_venues'),
    url(r'^view_booking.html/', views.view_booking, name='view_booking'),
    url(r'^get_reviews.html/', views.get_reviews, name='get_reviews'),
    url(r'^index1/', views.index1, name='index1'),
    url(r'admin_login/', views.admin_login, name='admin_login'),
    url(r'delete_venue/', views.delete_venue, name='delete_venue'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
