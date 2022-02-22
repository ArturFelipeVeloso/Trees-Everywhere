from django.db import models
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    joined = models.DateTimeField(verbose_name='Joined in')
    
    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
# Account model
class Account(models.Model):
    user = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created in')
    active = models.BooleanField(default=True, verbose_name='Active?',
                                    help_text='If you deselect this profile you will not be able to log in to the system.')
    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

