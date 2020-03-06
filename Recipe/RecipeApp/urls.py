from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('settings/', views.settings, name='settings'),
    path('settings/tags/add/', views.add_tag, name='add_tag'),
    path('settings/unit/add/', views.add_unit, name='add_unit'),
    path('settings/tags/delete/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('settings/unit/delete/<int:unit_id>/', views.delete_unit, name='delete_unit'),
    path('', include('django.contrib.auth.urls'))
]