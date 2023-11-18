from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<int:recipe_id>", recipe, name="recipe"),
    path("search", search, name="search"),
    path("create/recipe", create_recipe, name="create_recipe"),
    path("delete/recipe/<int:recipe_id>", delete_recipe, name="delete_recipe"),
    path("edit/recipe/<int:recipe_id>", edit_recipe, name="edit_recipe"),
    path("update/recipe", update_recipe, name="update_recipe"),
]
