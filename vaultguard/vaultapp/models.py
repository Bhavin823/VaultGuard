from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
import base64
from django.conf import settings

fernet = Fernet(settings.FERNET_KEY)

def encrypt_passowrd(password):
    encrypted_password = fernet.encrypt(password.encode()).decode()
    return encrypted_password

def decrypt_password(encrypted_password):
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
    return decrypted_password


# Create your models here.
class PasswordVault(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='passwordvault')
    website = models.CharField(max_length=255)
    username_of_website = models.CharField(max_length=255)
    password_of_website = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username}'s Password For {self.website}"
    