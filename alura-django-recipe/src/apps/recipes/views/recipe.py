from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.order_by("-created_at").filter(is_published=True)
    paginator = Paginator(recipes, 6)
    page = request.GET.get("page")
    recipes_per_page = paginator.get_page(page)
    data = {
        "recipes": recipes_per_page,
    }
    return render(request, "recipes/index.html", data)


def recipe(request, recipe_id):
    _recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {
        "recipe": _recipe,
    }
    return render(request, "recipes/recipe.html", data)


def create_recipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            ingredients = request.POST["ingredients"]
            how_to_cook = request.POST["how_to_cook"]
            time = request.POST["time"]
            recipe_yield = request.POST["recipe_yield"]
            category = request.POST["category"]
            picture = request.FILES["picture"]

            user = get_object_or_404(User, pk=request.user.id)
            _recipe = Recipe.objects.create(
                user=user,
                name=name,
                ingredients=ingredients,
                how_to_cook=how_to_cook,
                time=time,
                recipe_yield=recipe_yield,
                category=category,
                picture=picture,
            )
            _recipe.save()

            return redirect("dashboard")
        else:
            return render(request, "recipes/create_recipe.html")
    else:
        return redirect("index")


def delete_recipe(request, recipe_id):
    _recipe = get_object_or_404(Recipe, pk=recipe_id)
    _recipe.delete()
    return redirect("dashboard")


def edit_recipe(request, recipe_id):
    _recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {
        "recipe": _recipe,
    }
    return render(request, "recipes/edit_recipe.html", data)


def update_recipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            recipe_id = request.POST["recipe_id"]
            _recipe = Recipe.objects.get(pk=recipe_id)
            _recipe.name = request.POST["name"]
            _recipe.ingredients = request.POST["ingredients"]
            _recipe.how_to_cook = request.POST["how_to_cook"]
            _recipe.time = request.POST["time"]
            _recipe.recipe_yield = request.POST["recipe_yield"]
            _recipe.category = request.POST["category"]
            if "picture" in request.FILES:
                _recipe.picture = request.FILES["picture"]
            _recipe.save()
            return redirect("dashboard")
