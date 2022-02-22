from django.contrib import admin
from .models import Profile, Account

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about', 'joined')
  
  
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created', 'active')