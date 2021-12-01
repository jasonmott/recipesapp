from django.db.models.fields import EmailField
from django.http.response import HttpResponse
from .models import Customer
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegistrationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = [ 
            'email',
            'username',
        ]

        def save(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            Customer.create_user(
                email= email,
                username = username,
                password = password,
            )

            return HttpResponse('User was created')
