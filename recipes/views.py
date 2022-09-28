from django.shortcuts import render

template_home = 'recipes/pages/home.html'
template_recipe = 'recipes/pages/recipe-view.html'


def home(request):
    return render(request, template_home)


def recipe(request, id):
    return render(request, template_recipe)
