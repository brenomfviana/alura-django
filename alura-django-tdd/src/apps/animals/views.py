from animals.models import Animal
from django.shortcuts import render


def index(request):
    context = {"characteristics": None}
    if "search" in request.GET:
        animals = Animal.objects.all()
        searched_animal = request.GET["search"]
        characteristics = animals.filter(name__icontains=searched_animal)
        context = {"characteristics": characteristics}
    return render(request, "index.html", context)
