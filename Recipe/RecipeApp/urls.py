from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/new', views.new_recipe, name='new_recipe'),
    path('', include('django.contrib.auth.urls'))
]