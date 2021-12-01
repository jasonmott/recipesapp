from django.db import models
from django.db.models.deletion import CASCADE
from .possible_units import possible_units, possible_cuisine, possible_diets, grocery_aisles
from django.urls import reverse

class Tag(models.Model):
    information = models.CharField(max_length=100,unique=True)
    active = models.BooleanField(default=True,)

    class Meta:
        ordering = ['information']

    def __str__(self):
        return str(self.information)
    
class Receipe(models.Model):
    title = models.CharField(max_length=200)  
    receipe_id = models.IntegerField(blank=True,null=True) 
    cuisine = models.ManyToManyField('Cuisine', blank=True)
    diets = models.ManyToManyField('Diet', blank=True)
    servings = models.IntegerField(blank=True,null=True)
    instructions = models.TextField(blank=True,null=True) 
    summary = models.TextField(blank=True,null=True)
    prep_time = models.IntegerField(default=0,null=True)
    rating = models.FloatField(blank=True,default=None,null=True)
    number_of_reviews = models.IntegerField(default=0,null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    name_of_source = models.CharField(max_length=200,null=True) 
    source_URL = models.URLField(blank=True,null=True)
    calories = models.FloatField(blank=True,default=0)
    carbs = models.FloatField(blank=True,default=0)
    fat = models.FloatField(blank=True,default=0)
    protein = models.FloatField(blank=True,default=0)
    image_URL = models.URLField(blank=True,null=True) 
    ingredient = models.ManyToManyField('Ingredient', blank=True)
    ingredient_amount = models.ManyToManyField('IngredientAmount', blank=True, editable=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        # calling PostDetail pattern from the urls.py file. kwars is key word search
        return reverse("RecipeDetailView", kwargs={"pk": self.pk})

class Ingredient(models.Model):
    grocery_aisle = models.CharField(choices=grocery_aisles,max_length=100,blank=True, default=None,null=True)
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name.title())

class IngredientAmount(models.Model):
    receipe_name = models.ForeignKey(Receipe, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(blank=True)
    select_type_of_unit = models.CharField(choices=possible_units,max_length=100,default=None)

    def __str__(self):
        #return str(self.name)
        return f'{self.receipe_name} - {self.amount} {self.select_type_of_unit} {self.name}' 

class Cuisine(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name.title())

class Diet(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return str(self.name.title())