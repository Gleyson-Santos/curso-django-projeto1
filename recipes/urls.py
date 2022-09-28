from django.urls import path

from . import views  # from recipes import views

urlpatterns = [
    path('', views.home),
    path('recipes/<id>', views.recipe),
]
