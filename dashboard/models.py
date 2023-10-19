from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
 
class User(AbstractUser):
    admin = 0
    client = 1
    Employee_Fraud = 2
    Employee_full = 3
    Employee_Support = 4
    Acountant = 5
    Professor = 6
    ROLES = (
        (admin, 'admin'),
        (client, 'client'),
        (Employee_Fraud, 'Employee_Fraud'),
        (Employee_full, 'Employee_full'),
        (Employee_Support, 'Employee_Support'),
        (Acountant, 'Acountant'),
        (Professor, 'Professor'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)


class Userinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name    = models.CharField(max_length=200, unique=True)
    last_name    = models.CharField(max_length=200, unique=True)
    username    = models.CharField(max_length=200, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    phonenumber           = models.IntegerField()
    totaltransaction           = models.IntegerField(null=True)
    Businessphonenumber           = models.IntegerField(null=True)
    Businessemail           = models.EmailField(max_length=100, unique=True,null=True)
    totalammount  = models.IntegerField()
    disputes  = models.IntegerField()
    totaldisputesammount  = models.IntegerField()
    accceptedtrans  = models.IntegerField()
    declinetrans  = models.IntegerField()
    charbackcountrate          = models.IntegerField()
    volume  = models.IntegerField()
    limit  = models.IntegerField()
    declinetrans  = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Bin  = models.CharField(max_length=100)
    Lastfour  = models.CharField(max_length=100)
    ammount  = models.IntegerField()
    payout  = models.CharField(max_length=100)
    code  = models.IntegerField()
    accepted  = models.BooleanField(default=False)
    InternalTransactionid  = models.CharField(max_length=100)
    created_at    = models.DateTimeField(auto_now_add=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(Userinfo, on_delete=models.CASCADE, null=True)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
    
    
    