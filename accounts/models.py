from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10, unique = True)
    user_bio = models.CharField(max_length = 50)
    user_profile_img = models.ImageField(upload_to="profile")

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
    
