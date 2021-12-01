from django.urls import path
from . import views

app_name = "receipes_app"
urlpatterns = [

    #path("",views.GetHome.as_view(), name = "list_view"),
    path("", views.GetReceipeList.as_view()),
    path("<int:pk>/", views.GetReceipeDetail.as_view()),
   
]