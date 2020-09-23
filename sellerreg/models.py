from django.db import models
#from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse; 

class SellerProfile(models.Model):
    seller_name = models.CharField(max_length=30, blank=True)
    email_id = models.EmailField(max_length=50, blank=False, unique=True)
    birth_date = models.DateField(null=True, blank=False)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    gst_number = models.CharField(max_length=15, unique=True, blank=False, editable=True)
    phone_number = PhoneNumberField(blank=True, unique=True)
    comment = models.TextField(max_length=500, blank=True)
    rejected = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    
    def __str__(self):
        return self.seller_name
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('sellerdetails', args=[str(self.id)])
