from rest_framework import viewsets
from recipes.serializers import (
    IngredientSerializer,
    RecipeSerializer,
)
from recipes.models import (
    Ingredient,
    Recipe,
)

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
