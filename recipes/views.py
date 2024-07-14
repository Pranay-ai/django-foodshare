from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListByCategory(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Recipe.objects.filter(category=category)

class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'recipe_id'

class RecipeCreate(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
