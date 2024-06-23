from django.contrib import admin
from .models import PasswordVault

# Register your models here.
class PasswordVaultAdmin(admin.ModelAdmin):
    list_display = ['id','user','website','username_of_website']

admin.site.register(PasswordVault,PasswordVaultAdmin)