from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordVault(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='passwordvault')
    website = models.CharField(max_length=255)
    username_of_website = models.CharField(max_length=255)
    password_of_website = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s Password For {self.website}"
    