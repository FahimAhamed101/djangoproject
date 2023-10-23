from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.db.models.signals import post_save


ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drives Licence"),
    ("international_passport", "International Passport")
)


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) #123 345 789 102
    account_number = ShortUUIDField(unique=True,length=10, max_length=25, prefix="217", alphabet="1234567890") #2175893745837
    account_id = ShortUUIDField(unique=True,length=7, max_length=25, prefix="DEX", alphabet="1234567890") #2175893745837
    pin_number = ShortUUIDField(unique=True,length=4, max_length=7, alphabet="1234567890") #2737
    red_code = ShortUUIDField(unique=True,length=10, max_length=20, alphabet="abcdefgh1234567890") #2737
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")
    review = models.CharField(max_length=100, null=True, blank=True, default="Review")
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
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}"

class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="kyc", default="default.jpg")
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=40)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to="kyc", null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    signature = models.ImageField(upload_to="kyc")

    # Address
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # Contact Detail
    mobile = models.CharField(max_length=1000)
    fax = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"    

    
    class Meta:
        ordering = ['-date']



def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender, instance,**kwargs):
    instance.account.save()

post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)
