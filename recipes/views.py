from django.shortcuts import render

template_name_home = 'recipes/home.html'
template_name_contato = 'recipes/contato.html'
template_name_sobre = 'recipes/sobre.html'


def home(request):
    return render(request, template_name_home, context={
        'name': 'Gleyson Santos',
    })


def contato(request):
    return render(request, template_name_contato)


def sobre(request):
    return render(request, template_name_sobre)
