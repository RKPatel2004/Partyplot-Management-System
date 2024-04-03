from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected ForeignKey usage
    email = models.EmailField(max_length=50)
    phoneNo = models.CharField(max_length=10)  
    password = models.CharField(max_length=10,default='')
    def __str__(self):
        return "Customer ID: " + str(self.customer_id)


class Admin(models.Model):
    Admin_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE) 
    email = models.EmailField(max_length=50)
    phoneNo = models.CharField(max_length=10)  
    password = models.CharField(max_length=10,default='')
    def __str__(self):
        return self.name


class Venue(models.Model):
    venue_name = models.CharField(max_length=100,primary_key=True)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    amenities = models.TextField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=False)
    image = models.ImageField(upload_to='venue_images/', null=True, blank=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField() 
    booking_price = models.IntegerField() 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default='')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE,default='')
    def __str__(self):
        return str(self.date) 



    
class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)