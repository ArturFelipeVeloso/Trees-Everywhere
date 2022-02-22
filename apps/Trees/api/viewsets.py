from rest_framework import response, status, viewsets
import rest_framework

# Serializer
from .serializers import PlantedTreesSerializers

# Model import
from ..models import PlantedTrees

# Authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Planted Tree Viewset
class PlantedTreeViewsets(viewsets.ModelViewSet):
        # Authentication
        permission_classes = (IsAuthenticated, )
        authentication_classes = (TokenAuthentication, )
        
        def get_queryset(self):
                # Get user request
                user = self.request.user
                # Filter data
                queryset = PlantedTrees.objects.filter(user = user)
                # Return result
                return queryset
                
        serializer_class = PlantedTreesSerializers