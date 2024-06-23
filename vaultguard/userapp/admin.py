from django.contrib import admin
from .models import UserModel

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['user','firstname','lastname']

admin.site.register(UserModel,UserAdmin)