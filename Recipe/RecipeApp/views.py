from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect



def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('login/')  

def new_recipe(request):
    if request.user.is_authenticated:
        return render(request, 'new_recipe.html')