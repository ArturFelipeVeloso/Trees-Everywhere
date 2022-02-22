from rest_framework import serializers
from ..models import PlantedTrees

class PlantedTreesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlantedTrees
        fields = "__all__"