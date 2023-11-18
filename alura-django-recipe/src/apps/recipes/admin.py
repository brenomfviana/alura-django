from django.contrib import admin

from .models import Recipe


class RecipeListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "id",
        "name",
        "category",
        "time",
        "recipe_yield",
        "is_published",
        "picture",
        "created_at",
    )
    list_display_links = (
        "id",
        "name",
    )
    list_filter = (
        "category",
        "is_published",
    )
    list_editable = ("is_published",)
    search_fields = ("name",)


admin.site.register(Recipe, RecipeListAdmin)
