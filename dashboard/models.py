from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
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
    first_name    = models.CharField(max_length=200, )
    last_name    = models.CharField(max_length=200,)
    username    = models.CharField(max_length=200, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    phonenumber           = models.IntegerField(blank=True, null=True)
    totaltransaction           = models.IntegerField(null=True)
    Businessphonenumber           = models.IntegerField(null=True)
    Businessemail           = models.EmailField(max_length=100, unique=True,null=True)
    totalammount  = models.IntegerField(blank=True, null=True)
    disputes  = models.IntegerField(blank=True, null=True)
    totaldisputesammount  = models.IntegerField(blank=True, null=True)
    accceptedtrans  = models.IntegerField(blank=True, null=True)
    declinetrans  = models.IntegerField(blank=True, null=True)
    charbackcountrate          = models.IntegerField(blank=True, null=True)
    volume  = models.IntegerField(blank=True, null=True)
    limit  = models.IntegerField(blank=True, null=True)
    declinetrans  = models.IntegerField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superadmin        = models.BooleanField(default=False)

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'



    
    
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
    


    
    
    