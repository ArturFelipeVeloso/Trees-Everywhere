from django.forms import ModelForm
from .models import PlantedTrees

class PlantedTreesForm(ModelForm):
    class Meta:
        model = PlantedTrees
        fields = ['age', 'tree', 'about', 'location_lat', 'location_long']