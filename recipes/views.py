from django.http import HttpResponse
from django.shortcuts import render


def my_home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Gleyson Santos',
    })


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return render(request, 'temp.html')
