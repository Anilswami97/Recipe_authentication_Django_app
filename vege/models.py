from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=150)
    recipe_description = models.CharField(max_length=1000)
    recipe_image = models.ImageField(upload_to="vege/recipe_images/")

    def __str__(self)->str:
        return self.recipe_name
         
    