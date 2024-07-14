from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    instructions = serializers.JSONField()  # Ensure instructions are handled as JSON

    class Meta:
        model = Recipe
        fields = ['recipe_id', 'author_name', 'name', 'category', 'ingredients', 'instructions', 'image_url']
