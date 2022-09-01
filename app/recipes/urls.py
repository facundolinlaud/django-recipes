from __future__ import print_function
from django.conf import settings
from django.conf.urls import url
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from recipes import views

router = DefaultRouter()
router.register(r'api/recipes', views.RecipeViewSet, basename='recipes')
router.register(r'api/ingredients', views.IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
