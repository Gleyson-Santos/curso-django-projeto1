from django.shortcuts import render
from utils.recipes.factory import make_recipe

template_home = 'recipes/pages/home.html'
template_recipe = 'recipes/pages/recipe-view.html'

context_home = {
    'recipes': [make_recipe() for _ in range(10)]
}

context_recipe = {
    'recipe': make_recipe()
}


def home(request):
    return render(request, template_home, context_home)


def recipe(request, id):
    return render(request, template_recipe, context_recipe)
