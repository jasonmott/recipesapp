from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from .models import Tag, Receipe, Ingredient, Cuisine, Diet
from django.views import View
from .serializers import ReceipeListSerializer

class GetReceipeList(generics.ListAPIView):
    queryset = Receipe.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReceipeListSerializer

class GetReceipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipe.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReceipeListSerializer    

# class GetAllRecipes(View):
#     def get(self, request):
#         recipe = Receipe.objects.all()
#         cuisine = Receipe.objects.all(cuisine=recipe.cuisine)
#         diet = Receipe.objects.all(diet=recipe.diet)
#         print(cuisine)
#         return render(request, "receipes_app/all_receipes.html", {"query_set":recipe, "cuisines":cuisine, "diets":diet, "message":"Hello"})

