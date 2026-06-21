from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    # path('', views.myapp),
    re_path('pokedex/api/login', views.login),
    re_path('pokedex/api/signup', views.signup),
    re_path('pokedex/api/test_token', views.test_token),
    path('pokedex/api/', views.get_all_pokemon),
    path('pokedex/api/pokemon/<int:pokemon_id>/', views.get_pokemon),
    path('pokedex/api/post_pokemon/', views.post_pokemon),
]
