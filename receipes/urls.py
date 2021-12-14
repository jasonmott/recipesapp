"""receipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import CreateCustomer, WelcomeView
from receipes_app.models import Receipe, Cuisine, Diet, Ingredient, IngredientAmount
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.GetAllRecipes.as_view(), name = "list_view"),
    path("recipe/all/",views.ListAllRecipes.as_view(), name = "list_all_recipes"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name="RecipeDetailView"),
    path("recipe/cuisine/<cuisine>/",views.FilterByCuisine.as_view(), name="cuisine_view"),
    path("recipe/diet/<diet>/",views.FilterByDiet.as_view(), name="diet_view"),
    path("recipe/dishtype/<dish_type>/",views.FilterByDishType.as_view(), name="dish_type_view"),
    path("recipe/ingredient/<ingredient>/",views.FilterByIngredient.as_view(), name="ingredient_view"),
    path("recipe/search/<search_query>/",views.FilterByUserSearch.as_view(), name="search_view"),
    path("contactus/",views.ContactUs.as_view(), name = "contact_us_view"),
    path("signup/",views.SignUp.as_view(), name = "sign_up_view"),
    path("login/",views.UserLogin.as_view(), name = "login_view"),
    path('search/', views.SearchView.as_view(), name="search"),
]
