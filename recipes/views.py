from django.shortcuts import render

template_name_home = 'recipes/pages/home.html'


context_obj = {
    'name': 'Gleyson Santos',
}


def home(request):
    return render(request, template_name_home, context=context_obj)
