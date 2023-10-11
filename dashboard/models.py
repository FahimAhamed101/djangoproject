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

    