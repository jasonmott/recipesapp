from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from django.views import View 
from django.views.generic import DetailView, ListView
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
        all_recipes = Receipe.objects.all().order_by("-rating")
        recipe = Receipe.objects.get(id=kwargs['pk'])
        #print(recipe_cuisines)
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        recipe_ingredients = IngredientAmount.objects.filter(receipe_name=kwargs['pk'])
        print(recipe.cuisine)
        popular_recipes = Receipe.objects.filter(rating__gte=90.00).filter(number_of_reviews__gte=10).filter(cuisine="1").order_by("-rating")[:4]
        all_ingredients = Ingredient.objects.all()
        dish_type = DishType.objects.all()
        print(recipe)
        return render(request, "receipes_app/receipe_detail.html", {"query_set":recipe, "query_popular_receipes":popular_recipes, "query_cuisine":cuisine, "query_diet":diet, "query_ingredient_amount":recipe_ingredients, "query_dishtype":dish_type, "query_ingredients":all_ingredients, "query_all_recipes":all_recipes})

class FilterByCuisine(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(cuisine=kwargs["cuisine"]).order_by("-rating")
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByDiet(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(diets=kwargs["diet"]).order_by("-rating")
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByIngredient(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(ingredient=kwargs["ingredient"]).order_by("-rating")
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()
        return render(request, "receipes_app/all_recipes.html", {"query_set":recipe, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class FilterByDishType(View):
    
    def get(self, request, **kwargs):

        recipe = Receipe.objects.filter(dish_type=kwargs["dish_type"]).order_by("-rating")
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

        all_recipes = Receipe.objects.all().order_by("-rating")
        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()

        return render(request, "receipes_app/list_all_recipes.html", {"query_all_recipes":all_recipes, "query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class ContactUs(View):
    
    def get(self, request):

        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()

        return render(request, "receipes_app/contact.html", {"query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})


class UserLogin(View):
    
    def get(self, request):

        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()

        return render(request, "receipes_app/login.html", {"query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class SignUp(View):
    
    def get(self, request):

        cuisine = Cuisine.objects.all()
        diet = Diet.objects.all()
        dish_type = DishType.objects.all()
        all_ingredients = Ingredient.objects.all()

        return render(request, "receipes_app/signup.html", {"query_cuisine":cuisine, "query_diet":diet, "query_dishtype":dish_type, "query_ingredients":all_ingredients})

class SearchView(ListView):
	model = Receipe
	template_name = 'receipes_app/recipe_search.html'
	#context_object_name = 'all_search_results'

	def get_context_data(self, **kwargs):
		#print(self.request.GET.get('search'))
		context = super(SearchView, self).get_context_data(**kwargs)
		print("This is the context",context, type(context))
		query = self.request.GET.get('search')
		if query:
			postresult = Receipe.objects.filter(title__contains=query)
			context['all_search_results'] = postresult
		else:
			context['all_search_results'] = None
		#print(result)
		cuisine = Cuisine.objects.all()
		diet = Diet.objects.all()
		dish_type = DishType.objects.all()
		all_ingredients = Ingredient.objects.all()
		context['query_cuisine'] = cuisine
		context['query_diet'] = diet
		context['query_dishtype'] = dish_type
		context['query_ingredients'] = all_ingredients
		return context
        # Git






        