from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(null=True, blank=True,max_length=20)
    address =models.CharField(max_length=300,blank=False,null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number','address']  

    def __str__(self):
        return self.email
