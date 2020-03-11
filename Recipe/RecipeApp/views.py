from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .forms import Tag_Form,Unit_Form

def home(request):
    if request.user.is_authenticated:

        search_tag = request.GET.get('search', None)

        if search_tag:
            recipes_search_name = Recipe.objects.filter(name__contains=search_tag)
            recipes_search_description = Recipe.objects.filter(description__contains=search_tag)
            recipes_search_tags = Recipe.objects.filter(tags__tag__contains=search_tag)
            recipes_all = recipes_search_name.union(recipes_search_description,recipes_search_tags)
        else:
            recipes_all = Recipe.objects.all()
        

        page = request.GET.get('page', 1)

        paginator = Paginator(recipes_all, 12)

        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

        context = {'home': 'active', 'recipes': recipes}
        return render(request, 'home.html', context)
    else:
        return HttpResponseRedirect('login/')  

def add_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST': 

            recipe_name = request.POST['recipe_name']
            recipe_duration = request.POST['recipe_duration']
            recipe_serving = request.POST['recipe_serving']
            recipe_description = request.POST['recipe_description']
            recipe_note = request.POST['recipe_note']
            instruction_count = int(request.POST['instruction_count'])
            ingredient_count = int(request.POST['ingredient_count'])
            recipe_tags = request.POST.getlist('tags')

            new_recipe = Recipe(name=recipe_name,duration=recipe_duration,serving=recipe_serving,description=recipe_description,note=recipe_note)
            new_recipe.save()

            for recipe_tag in recipe_tags:
                tag = Tag.objects.get(tag=recipe_tag)
                new_recipe.tags.add(tag)
            

            for i in range(ingredient_count):
                ingredient_name = request.POST['ingredient_name_' + str(i)]
                ingredient_amount = request.POST['ingredient_amount_' + str(i)]
                ingredient_unit = request.POST['ingredient_unit_select_' + str(i)]

                unit = Unit.objects.get(id=ingredient_unit)
                new_ingredient = Ingredient(name=ingredient_name,amount=ingredient_amount,unit=unit,recipe=new_recipe)
                new_ingredient.save()

            
            for i in range(instruction_count):
                ingredient_text = request.POST['text_' + str(i)]
                ingredient_sort = i

                new_ingredient = Instruction(text=ingredient_text,sort=ingredient_sort,recipe=new_recipe)
                new_ingredient.save()

            new_recipe.save()
            return redirect('view_recipe', recipe_slug=new_recipe.slug)
            
        if request.method == 'GET':    
            units_all = Unit.objects.all()    
            tags_all = Tag.objects.all()
            context = {'add_recipe': 'active', 'units': units_all, 'tags': tags_all,}
            return render(request, 'add_recipe.html', context)

def view_recipe(request,recipe_slug):

    recipe = Recipe.objects.get(slug=recipe_slug)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    instructions = Instruction.objects.filter(recipe=recipe).order_by('sort')

    context = {'recipe': recipe, 'ingredients': ingredients,'instructions': instructions}
    return render(request, 'view_recipe.html', context)

def edit_recipe(request,recipe_slug):

    recipe = Recipe.objects.get(slug=recipe_slug)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    instructions = Instruction.objects.filter(recipe=recipe).order_by('sort')

    context = {'recipe': recipe, 'ingredients': ingredients,'instructions': instructions}
    return render(request, 'add_recipe.html', context)

def settings(request):
    if request.user.is_authenticated:
        tag_form = Tag_Form()
        unit_form = Unit_Form()
        units_all = Unit.objects.all()
        tags_all = Tag.objects.all()

        context = {'settings': 'active', 'units': units_all, 'tags': tags_all,'tag_form': tag_form, 'unit_form': unit_form}
        return render(request, 'settings.html', context)

def add_tag(request):
    if request.user.is_authenticated:
        if request.method == 'POST':        
            form = Tag_Form(request.POST)
            if form.is_valid():
                tag = Tag(tag=form.cleaned_data['tag'])
                tag.save()
        return HttpResponseRedirect('/settings')  

def delete_tag(request,tag_id):
    if request.user.is_authenticated:
        tag = Tag.objects.get(id=tag_id)
        tag.delete()
        return HttpResponseRedirect('/settings')  

def add_unit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':        
            form = Unit_Form(request.POST)
            if form.is_valid():
                unit = Unit(name=form.cleaned_data['name'])
                unit.save()
        return HttpResponseRedirect('/settings')  

def delete_unit(request,unit_id):
    if request.user.is_authenticated:
        unit = Unit.objects.get(id=unit_id)
        unit.delete()
        return HttpResponseRedirect('/settings')  