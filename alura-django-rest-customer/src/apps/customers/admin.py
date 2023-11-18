from customers.models import Customer
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "cpf",
        "cellphone",
        "active",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = ("name", "cpf")
    list_filter = ("active",)
    list_editable = ("active",)
    ordering = ("name",)
    list_per_page = 25


admin.site.register(Customer, CustomerAdmin)
