from django.urls import path
from . import views

urlpatterns = [
    path('fitness',views.fitness , name="fitness"),
    path('cardio',views.cardio , name="cardio"),
    path('poitrine',views.poitrine , name="poitrine"),
    path('dorsau',views.dorsau , name="dorsau"),
    path('biceps',views.biceps , name="biceps"),
    path('epaule',views.epaule , name="epaule"),
    path('jambe',views.jambe , name="jambe"),
    path('conseil_med',views.conseil_med , name="conseil_med"),
]