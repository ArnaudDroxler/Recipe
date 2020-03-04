from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

from .forms import Tag_Form,Unit_Form

def home(request):
    if request.user.is_authenticated:
        context = {'home': 'active'}
        return render(request, 'home.html', context)
    else:
        return HttpResponseRedirect('login/')  

def add_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':        
            pass
        if request.method == 'GET':    
            units_all = Unit.objects.all()    
            tags_all = Tag.objects.all()
            context = {'add_recipe': 'active', 'units': units_all, 'tags': tags_all,}
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