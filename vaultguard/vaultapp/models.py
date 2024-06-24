from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
import base64
from django.conf import settings

def encrypt_passowrd(password):
    secret_key = settings.SECRET_KEY.encode()
    fernet = Fernet(secret_key)
    encrypted_passowrd = fernet.encrypt(password.encode()).decode()
    return encrypted_passowrd

def decrypt_password(encrypted_passowrd):
    secret_key = settings.SECRET_KEY.encode()
    fernet = Fernet(secret_key)
    decrypted_password = fernet.decrypt(encrypted_passowrd.encode()).decode()
    return decrypted_password


# Create your models here.
class PasswordVault(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='passwordvault')
    website = models.CharField(max_length=255)
    username_of_website = models.CharField(max_length=255)
    password_of_website = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username}'s Password For {self.website}"
    