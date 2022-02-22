# Basic imports
from django.urls import path, include

# View imports
from .views import home, viewPlantedTree, addPlantedTree, editPlantedTree

# API imports
from rest_framework import routers
from .api.viewsets import PlantedTreeViewsets

# Route API
route = routers.DefaultRouter()
route.register(r'plantedtree', PlantedTreeViewsets, basename = 'Planted Tree')

# URLs
urlpatterns = [
    # Site URL
    path('', home, name="home"),
    path('add/', home, name="home"),
    path('viewplantedtree/<int:planted_tree_id>/', viewPlantedTree, name="viewPlantedTree"),
    path('editplantedtree/<int:planted_tree_id>/', editPlantedTree, name="editPlantedTree"),
    path('addplantedtree/', addPlantedTree, name="addPlantedTree"),

    # API URL
    path('api/', include(route.urls), name="api-trees"),
]
