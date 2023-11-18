from django.contrib import admin

from .models import Person


class PersonListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "id",
        "name",
        "email",
    )
    list_display_links = (
        "id",
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )


admin.site.register(Person, PersonListAdmin)
