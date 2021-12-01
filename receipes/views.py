from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from django.views import View 
from django.views.generic import DetailView
from django.http import HttpResponse
from receipes_app.models import Receipe, Cuisine, Diet, IngredientAmount

class GetAllCuisines(View):

    model = Cuisine
    
    def get(self, request):
        cuisine_type = Cuisine.objects.all()
        return render(request, "receipes_app/index.html", {"query_cuisine":cuisine_type})

class GetAllDiets(View):

    model = Diet
    
    def get(self, request):
        diet_type = Diet.objects.all()
        return render(request, "receipes_app/index.html", {"query_diet":diet_type})


class GetAllRecipes(View):
    
    def get(self, request):
        recipe = Receipe.objects.all()
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        ingredient = IngredientAmount.objects.all()
        return render(request, "receipes_app/index.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})

class RecipeDetailView(DetailView):

    model = Receipe

    def get(self, request, **kwargs):
        print(kwargs)
        recipe = Receipe.objects.get(id=kwargs['pk'])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        print(cuisine)
        return render(request, "receipes_app/receipe_detail.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})

class FilterByCuisine(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(cuisine=kwargs["cuisine"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        print(recipe)
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})

class FilterByDiet(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(diets=kwargs["diet"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        print(recipe)
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})

class FilterByIngredient(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(ingredient=kwargs["ingredient"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        print(recipe)
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})