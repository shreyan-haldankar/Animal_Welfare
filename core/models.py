from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class Donation(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField( max_length=1000)
    city = models.CharField( max_length= 200)
    state = models.CharField(max_length=100)  
    zipcode = models.IntegerField()

    card_name = models.CharField(max_length=100)
    card_number = models.IntegerField()

    exp_month = models.CharField(max_length=50)
    exp_year = models.IntegerField()

    cvv = models.IntegerField()
    donationAmount  = models.IntegerField()

    def __str__(self):
        return str(self.donationAmount)



