from rest_framework import serializers
from .models import Receipe, Ingredient

class ReceipeListSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Receipe
        fields = [
            "pk",
            "title",
            "receipe_id",
            "cuisine",
            "diets",
            "servings",
            "instructions",
            "summary",
            "tag",
            "name_of_source",
            "source_URL",
            "calories",
            "carbs",
            "fat",
            "protein",
            "image_URL",
            #"prep_time",
            "ingredient",
            #"rating",
            ]
        extra_kwargs = {
            "receipe_id": {"required": False},
            "cuisine": {"required": False},
            "diets": {"required": False},
            "servings": {"required": False},
            "instructions": {"required": False},
            "summary": {"required": False},
            "tag": {"required": False},
            "name_of_source": {"required": False},
            "source_URL": {"required": False},
            "calories": {"required": False},
            "carbs": {"required": False},
            "fat": {"required": False},
            "protein": {"required": False},
            "image_URL": {"required": False},
            #"prep_time": {"required": False},
            "ingredient": {"required": False},
            #"rating": {"required": False},
        }