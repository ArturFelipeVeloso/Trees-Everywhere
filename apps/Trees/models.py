from django.db import models
from django.contrib.auth.models import User

# Plant Model
class Plant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name") 
    scientific_name = models.CharField(max_length=200, verbose_name="Scientific Name") 
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'
        
# PlantedTree Model
class PlantedTrees(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(verbose_name='Age')
    planted_at = models.DateTimeField(verbose_name='Planted at', blank=True, null=True)
    tree = models.ForeignKey(Plant, verbose_name="Plant", blank=True, null=True, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    location_lat = models.DecimalField(verbose_name='Lat', max_digits=22, decimal_places=16, blank=True, null=True)
    location_long = models.DecimalField(verbose_name='Long', max_digits=22, decimal_places=16, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Planted Tree'
        verbose_name_plural = 'Planted Trees'
        