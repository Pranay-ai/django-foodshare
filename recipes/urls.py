from django.urls import path
from .views import RecipeListByCategory, RecipeDetail, RecipeCreate

urlpatterns = [
    path('recipes/category/<str:category>/', RecipeListByCategory.as_view(), name='recipes-by-category'),
    path('recipes/<uuid:recipe_id>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/create/', RecipeCreate.as_view(), name='recipe-create'),
]
