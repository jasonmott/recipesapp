from django.contrib import admin

#from receipes.receipes_app.models import Ingredient, Receipe
from .models import Receipe, Ingredient, Tag, IngredientAmount, Cuisine, Diet

# Register your models here.
admin.site.register(Receipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(IngredientAmount)
admin.site.register(Cuisine)
admin.site.register(Diet)

