from django.db import models

# Create your models here.
class RestaurantPostOffer(models.Model):
    description_text = models.CharField(max_length=200)
    initial_quantity = models.IntegerField(default=0) 
    pub_date = models.DateTimeField('date published')
    expiry_date = models.DateTimeField('date expired')
    
class RestaurantStoryOffer(models.Model):
    description_text = models.CharField(max_length=200)
    initial_quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published') 
    expiry_date = models.DateTimeField('date expired')

class StudentOffer(models.Model):
    restaurant_text = models.CharField(max_length=200)
    offer_type_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    acquired_date = models.DateTimeField('date acquired')
    expiry_date = models.DateTimeField('date expired')

class StudentOffer(models.Model):
    restaurant_text = models.CharField(max_length=200)
    offer_type_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    acquired_date = models.DateTimeField('date acquired')
    expiry_date = models.DateTimeField('date expired')
    
