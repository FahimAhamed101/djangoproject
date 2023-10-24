from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
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
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username