from django import template

from receipes_app.models import Cuisine, Diet, DishType, Ingredient

register = template.Library()


@register.simple_tag()
def get_meals():
    return DishType.objects.all()
def get_diets():
    return Diet.objects.all()
def get_cuisines():
    return Cuisine.objects.all()
def get_ingredients():
    return Ingredient.objects.all()