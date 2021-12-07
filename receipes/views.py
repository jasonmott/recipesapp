from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from django.views import View 
from django.views.generic import DetailView
from django.http import HttpResponse
from receipes_app.models import Receipe, Cuisine, Diet, IngredientAmount, DishType, Ingredient
from django.db.models import Q
import random

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


# class GetAllRecipes(View):
    
#     def get(self, request):
#         count_receipes = Receipe.objects.count()
#         random_number = random.randint(1,count_receipes)
#         print(random_number)
#         # random_recipe = Receipe.objects.get(id=random_number)
#         recipe = Receipe.objects.all()
#         cuisine = Cuisine.objects.all()
#         diet = Diet.objects.all()
#         ingredient = IngredientAmount.objects.all()
#         return render(request, "receipes_app/index.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet})

class GetAllRecipes(View):
    
    def get(self, request):

        count_receipes = Receipe.objects.count()
        random_number1 = random.randint(1,count_receipes)
        random_number2 = random.randint(1,count_receipes)
        random_number3 = random.randint(1,count_receipes)
        print(random_number1, random_number2, random_number3)
        # random_recipe = Receipe.objects.get(id=random_number)
        recipe1 = Receipe.objects.get(id=random_number1)
        recipe2 = Receipe.objects.get(id=random_number2)
        recipe3 = Receipe.objects.get(id=random_number3)
        popular_recipe1 = Receipe.objects.filter(rating__gte=90.00).filter(number_of_reviews__gte=10).order_by("-rating")[:4]
        popular_recipe2 = Receipe.objects.filter(rating__gte=90.00).filter(number_of_reviews__gte=10).order_by("-rating")[5:9]
        popular_recipe3 = Receipe.objects.filter(rating__gte=90.00).filter(number_of_reviews__gte=10).order_by("-rating")[10:14]
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        all_ingredients = Ingredient.objects.all()
        dish_type = DishType.objects.all()
        return render(request, "receipes_app/index.html", {"recipe_1":recipe1, "recipe_2":recipe2, "recipe_3":recipe3, "query_cuisine":cuisine, "query_diet":diet, "popular_recipe1":popular_recipe1, "popular_recipe2":popular_recipe2, "popular_recipe3":popular_recipe3, "query_dishtype":dish_type, "query_ingredients":all_ingredients})


class RecipeDetailView(DetailView):

    model = Receipe

    def get(self, request, **kwargs):
        all_recipes = Receipe.objects.all()
        recipe = Receipe.objects.get(id=kwargs['pk'])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        recipe_ingredients = IngredientAmount.objects.filter(receipe_name=kwargs['pk'])
        all_ingredients = Ingredient.objects.all()
        dish_type = DishType.objects.all()
        # popular_recipe1 = Cuisine.objects.get(id=kwargs['pk'])
        # print(popular_recipe1)
        return render(request, "receipes_app/receipe_detail.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_ingredient_amount":recipe_ingredients, "query_dishtype":dish_type, "query_ingredients":all_ingredients, "query_all_recipes":all_recipes})

class FilterByCuisine(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(cuisine=kwargs["cuisine"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByDiet(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(diets=kwargs["diet"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByIngredient(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(ingredient=kwargs["ingredient"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByDishType(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(dish_type=kwargs["dish_type"])
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByUserSearch(View):
    
    def get(self, request, **kwargs):

        user_query = (kwargs["search_query"])
        print(user_query)
        result_lookup = (Q(title__icontains=user_query) | Q(summary__icontains=user_query))
        search_query = Receipe.objects.filter(result_lookup)
        print(search_query)
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":search_query, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})


class ListAllRecipes(View):

    def get(self, request, **kwargs):

        all_recipes = Receipe.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_all_recipes":all_recipes})




        