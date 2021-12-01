from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm
from .models import Customer
from django.views import View
from django.urls import reverse

# Create your views here.

class CreateCustomer(View):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'

    def get(self,request):
        form =self.form_class
        return render(request, self.template_name, {'form':form, 'message':'Hello, please sign up.'}) 

    def post(self,request):
        form =self.form_class(request.POST)
        print(form)
        if form.is_valid():
            print("This is valid")
            form.save()
            return HttpResponseRedirect(reverse('welcome'))
        else:
            return render(request, self.template_name, {'form':form, 'message':'Registration Form is invalid'})

class WelcomeView(View):
    template_name = 'accounts/welcome.html'

    def get(self, request):
        
        return render(request, self.template_name, {'message':'Registration was successful.'})
