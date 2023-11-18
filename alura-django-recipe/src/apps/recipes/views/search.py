from django.shortcuts import render
from recipes.models import Recipe


def search(request):
    recipes = Recipe.objects.order_by("-created_at").filter(is_published=True)
    if "search" in request.GET:
        name = request.GET["search"]
        if name:
            recipes = recipes.filter(name__icontains=name)
    data = {
        "recipes": recipes,
    }
    return render(request, "recipes/search.html", data)
