from django.contrib import admin
from .models import Admin,Customer,Venue, Booking, Review


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'email', 'phoneNo', 'password')


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('event_id', 'name', 'time_period', 'attendees', 'organizer_name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'date', 'booking_price', 'customer_id', 'get_venue_name')

    def get_venue_name(self, obj):
        return obj.venue.venue_name

    get_venue_name.short_description = 'Venue Name'


# @admin.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('feedback_id', 'rating', 'date', 'booking_id')

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('payment_id', 'price', 'payment_method')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'location', 'capacity', 'amenities', 'pricing', 'availability')


@admin.register(Admin)
class AdminuserAdmin(admin.ModelAdmin):
    list_display = ('Admin_id', 'name', 'email', 'phoneNo', 'password')
    def Admin_id(self, obj):
        return obj.Admin_id

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'review_text', 'created_at')