import uuid
from django.db import models

class Recipe(models.Model):
    recipe_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
