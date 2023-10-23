from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.

    
    
class Transaction(models.Model):
    
    Bin  = models.CharField(max_length=100)
    Lastfour  = models.CharField(max_length=100)
    ammount  = models.IntegerField()
    payout  = models.CharField(max_length=100)
    code  = models.IntegerField()
    accepted  = models.BooleanField(default=False)
    InternalTransactionid  = models.CharField(max_length=100)
    created_at    = models.DateTimeField(auto_now_add=True)
    


    
    
    