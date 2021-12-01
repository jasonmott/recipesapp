from django import forms
from django.db.models.fields import EmailField
from django.http.response import HttpResponse
from .models import Receipe
from accounts.models import Customer, CustomerManager
from django.contrib.auth.forms import UserCreationForm

class ReceipeForm(forms.ModelForm):

    class Meta:
        model = Receipe
        fields = [
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
            "prep_time",
            "ingredients",
            "rating",
        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
    
    def save(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        Customer.create_user(
            email = email,
            username = username,
            password = password,
        )
        return HttpResponse("User was created.")