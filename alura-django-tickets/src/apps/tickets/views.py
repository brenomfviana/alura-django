from django.shortcuts import render
from tickets.forms import PersonForms, TicketForms


def index(request):
    form = TicketForms()
    person_form = PersonForms()
    context = {"form": form, "person_form": person_form}
    return render(request, "index.html", context)


def review_query(request):
    if request.method == "POST":
        form = TicketForms(request.POST)
        person_form = PersonForms(request.POST)
        if form.is_valid():
            context = {"form": form, "person_form": person_form}
            return render(request, "review.html", context)
        else:
            print("Form inválido")
            context = {"form": form, "person_form": person_form}
            return render(request, "index.html", context)
