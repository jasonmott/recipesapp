from django.core.management.base import BaseCommand, CommandError
import requests
from receipes_app.models import Receipe, Ingredient, Tag, Cuisine, Diet, IngredientAmount, DishType

class Command(BaseCommand):

    def handle(self, *args, **options):
        API_Key = "d21884ddb6024d8983e03760cd6cd479"    
        #Remove API key 
        api_auth = {'apiKey':API_Key}
        cuisine_selection = {'breakfast'}
        spoonacular_parameters = {'apiKey': API_Key,'limitLicense': True,'query': cuisine_selection,'number': 100}
        spoonacular_url = "https://api.spoonacular.com/recipes/complexSearch?"
        spoonacular_data = requests.get(spoonacular_url, params=spoonacular_parameters) 
        #print(spoonacular_data.url)
        result = spoonacular_data.json()
        print(result)

        receipe_info = result['results']
        #Below loops throught receipe_info for receipe_id and stores in a list
        receipe_id_list = [receipe_id["id"] for receipe_id in receipe_info]
        receipe_info_url = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=true"
        # Below creates a list to store receipe information from the receipe_info_url query
        full_receipe_contents = []
        #Below retrieves each receipe id from the receipe_id_list
        for rec_id in receipe_id_list:
            receipe_info_query = requests.get(receipe_info_url.format(rec_id), params=api_auth)
            receipe_detail = receipe_info_query.json()
            # Below command append the receipe_detail to the full_receipe_contents list
            full_receipe_contents.append(receipe_detail) 

        # Below performs a loop for each receipe in full_receipe_contents
        for rec in full_receipe_contents:
            # Using .get() because we are dealing with dictionary - Pulling nutrients from nutrition
            list_of_nutrition = rec.get('nutrition')
            nutrients = list_of_nutrition.get('nutrients')
            rec_name = rec.get('title')
            #list_of_dish_type = rec.get('dishTypes')
            # Using [] because contents of nutrients is a list - Pulls calories, fat, carbs, and protein
            calories_dict = nutrients[0]
            fat_dict = nutrients[1]
            carbs_dict = nutrients[3]
            protein_dict = nutrients[8]
            # Below is to pull cuisines, diets, and ingredients from the receipe
            receipe_cuisines = rec['cuisines']
            receipe_diets = rec['diets']
            receipe_ingredients = rec['extendedIngredients']
            receipe_dish_types = rec['dishTypes']

            rec, created = Receipe.objects.get_or_create(
                title = rec['title'],
                receipe_id = rec['id'],
                servings = rec['servings'],
                instructions = rec['instructions'],
                summary = rec['summary'],
                image_URL = rec['image'],
                prep_time = rec['readyInMinutes'],
                rating = rec['spoonacularScore'],
                number_of_reviews = rec['aggregateLikes'],
                #tag = rec['tag'],
                name_of_source = rec['sourceName'],
                source_URL = rec['sourceUrl'],
                # Calories,fat,carbs,protein information are in a dictionary so need to use get()
                calories = calories_dict.get('amount'),
                fat = fat_dict.get('amount'),
                carbs = carbs_dict.get('amount'),
                protein = protein_dict.get('amount'),
            )
            
            # for category in full_receipe_contents:
            #     print(category)
            for dish_type in receipe_dish_types:
                try:
                    dish_type = DishType.objects.get(dish_type)
                except:
                    print(f"{dish_type} did not work")
                dish_type, created = DishType.objects.get_or_create(
                    name = dish_type,
                )
                ####### Need to add cuisine to receipe through Receipe.cuisine
                rec.dish_type.add(dish_type)

            for cuisine in receipe_cuisines:
                try:
                    cuisine = Cuisine.objects.get(cuisine)
                except:
                    print(f"{cuisine} did not work")
                cuisine, created = Cuisine.objects.get_or_create(
                    name = cuisine,
                )
                ####### Need to add cuisine to receipe through Receipe.cuisine
                rec.cuisine.add(cuisine)

            for diet in receipe_diets:
                try:
                    diet = Diet.objects.get(diet)
                except:
                    print(f"{diet} did not work")
                diet, created = Diet.objects.get_or_create(
                    name = diet,
                )
                rec.diets.add(diet)

            for ingredient in receipe_ingredients:
                ing_name = ingredient['name']
                ing_amount = ingredient['amount']
                ing_unit = ingredient['unit']
                try:
                    value_ingredient = ingredient['name']
                except:
                    print(f"{value_ingredient} did not work")
                ingredient, created = Ingredient.objects.get_or_create(
                    name = value_ingredient,
                )                
                rec.ingredient.add(ingredient)
                print(ingredient)

                #Issue is on the line below where it returns 2 items
                ingredient_id = Ingredient.objects.get(name=ing_name)
                receipe_id = Receipe.objects.get(title=rec_name)

                ingredient, created = IngredientAmount.objects.get_or_create(
                    receipe_name = receipe_id,
                    name = ingredient_id,
                    amount = ing_amount,
                    select_type_of_unit = ing_unit,
                )

            print(rec, created)

